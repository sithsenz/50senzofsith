## General Structure

`Code.gs` contains all the general JS codes that are used throughout the website.
JS codes that are specific to each webpage are contained inside *html* files with ***js*** prefix.
>js-Laporan.html $$\rightarrow$$ laporan.html  
>js-Barangan.htm $$\rightarrow$$ barangan.html

### Building Webpage
So far `lampiran` is not used.

```js
function binaLaman(namaFail, lampiran){
  const laman = HtmlService.createTemplateFromFile(namaFail);

  if (lampiran){
    let indeks = Object.keys(lampiran);

    indeks.forEach((i)=>{
      laman[i] = lampiran[i];
    });
  }

  return laman.evaluate();
}
```

### Routes to Each Webpage

```js
const Alamat = {
  jalan: function(taman, fungsi){
    Alamat[taman] = fungsi;
  }
}


function doGet(e){
  Alamat.jalan("laporan", binaLamanLaporan);
  Alamat.jalan("barangan", binaLamanBarangan);
  Alamat.jalan("pembekal", binaLamanPembekal);
  Alamat.jalan("padanan", binaLamanPadanan);
  Alamat.jalan("baru", binaLamanBaru);
  Alamat.jalan("kemaskini", binaLamanKemaskini);

  if(e.parameter.laman){
    return Alamat[e.parameter.laman]();
  } else {
    return HtmlService.createTemplateFromFile("kemaskini").evaluate();
  }
}
```

### Loading Page
Each webpage usually starts with reading data from specified range after a successful `DOMContentLoaded` event.

```js
document.addEventListener('DOMContentLoaded', ()=>{
  google.script.run.withSuccessHandler(binaJadualLaporan).ambilData("Laporan");
});
```

# Create New Data

```js
function tambahPObaru(dataPO, dataTerperinci){
  const hamparan = SpreadsheetApp.openById("spreadsheet ID");
  const lembaranPO = hamparan.getSheetByName("PO");
  const lembaranTerperinci = hamparan.getSheetByName("PO Terperinci");

  lembaranPO.appendRow(dataPO);
  dataTerperinci.forEach(rekod => {
    lembaranTerperinci.appendRow(rekod);
  });

  TerikatRekodLPO.onEdit();

  cetakPO(dataPO[0]);
}
```

## New Entry Form

```js
function simpanPilihan(dataDariGoogleSheet, dataPertama){
  if (dataPertama === "dataPilihanRujUnit"){
    dataPilihanRujUnit = dataDariGoogleSheet.dataLemb1;
    dataPilihanJenisPerolehan = dataDariGoogleSheet.dataLemb2;
    binaSenaraiPilihan("senaraiRujUnit", dataPilihanRujUnit);
    binaSenaraiPilihan("senaraiJenisPerolehan", dataPilihanJenisPerolehan);
  } else if (dataPertama === "dataPilihanKodAgihan"){
    dataPilihanKodAgihan = dataDariGoogleSheet.dataLemb1;
    dataPilihanBarangan = dataDariGoogleSheet.dataLemb2;
    binaSenaraiPilihan("kodAgihan", dataPilihanKodAgihan);
    binaSenaraiPilihan("senaraiBaranganBaru", dataPilihanBarangan);
  } else {
    dataPilihanPembekal = dataDariGoogleSheet;
    binaSenaraiPilihan("senaraiPembekal1", dataPilihanPembekal);
    binaSenaraiPilihan("senaraiPembekal2", dataPilihanPembekal);
    binaSenaraiPilihan("senaraiPembekal3", dataPilihanPembekal);
  }
}


function binaSenaraiPilihan(idSenarai, data){
  const senarai = ambil(idSenarai);

  while (senarai.hasChildNodes()){
    senarai.removeChild(senarai.firstChild);
  }
  data.forEach(barisDalamData => {
    let pilihan = buat("option");
    pilihan.textContent = barisDalamData[0];
    senarai.appendChild(pilihan);
  });
}
```

## New Data Manipulation

```js
function tambahBaris(){
  let mesej = "";
  let badanJadual = ambil("badan-jadual-baru");
  let templat = ambil("templat-jadual").content;
  let barang = ambil("mintaBarangBaru");
  let kuantiti = ambil("mintaKuantitiBaru");
  let harga = ambil("mintaHargaBaru");

  mesej = kuantiti.validity.patternMismatch ? mesej + "Format kuantiti tidak sah. " : mesej;
  mesej = harga.validity.patternMismatch ? mesej + "Format harga tidak sah. " : mesej;

  if (mesej.length > 0){
    const kotakMesejPengesahanData = ambil("kotakMesejPengesahanData");
    const kotakMesej = bootstrap.Toast.getOrCreateInstance(kotakMesejPengesahanData);
    ambil("mesejPengesahanData").textContent = mesej;
    kotakMesej.show();
  } else {
    let barisBaru = templat.cloneNode(true);
    let barangBaru = barisBaru.querySelector(".dataBarangan");
    let kuantitiBaru = barisBaru.querySelector(".dataKuantiti") ;
    let hargaBaru = barisBaru.querySelector(".dataHargaSeunit");

    barangBaru.textContent = barang.value;
    kuantitiBaru.textContent = kuantiti.value;
    hargaBaru.textContent = harga.value;

    badanJadual.appendChild(barisBaru);

    barang.value = "";
    kuantiti.value = "";
    harga.value = "";

    let bilJadual = document.querySelectorAll(".dataBil");
    bilJadual.forEach(b => {b.textContent = b.parentNode.rowIndex});
    
    jumlahkanBaris();
  }
}


function padamkanBaris(butang){
  let barisIni = butang.parentNode.parentNode;
  let jadualIni = barisIni.parentNode.parentNode;
  jadualIni.deleteRow(barisIni.rowIndex);

  let bilJadual = document.querySelectorAll(".dataBil");
  bilJadual.forEach(b => {b.textContent = b.parentNode.rowIndex});
    
  jumlahkanBaris();
}


function jumlahkanBaris(){
  const badanJadual = ambil("badan-jadual-baru");
  const jumBaris = badanJadual.rows.length;
  let jumKeseluruhan = 0;

  for (let i=0; i<jumBaris; i++){
    let kuantitiBaris = badanJadual.rows[i].cells[2].textContent;
    let hargaBaris = badanJadual.rows[i].cells[3].textContent * 100;
    let jumlahSebaris = kuantitiBaris * hargaBaris / 100;
    badanJadual.rows[i].cells[4].textContent = jumlahSebaris.toFixed(2).replace(/\B(?=(\d{3})+(?!\d))/g, ",");
    jumKeseluruhan += jumlahSebaris;
  }

  ambil("jumlahKeseluruhan").textContent = jumKeseluruhan.toFixed(2).replace(/\B(?=(\d{3})+(?!\d))/g, ",");
}
```

# Read Data

```js
function ambilData(lemb1, lokasi1, lemb2, lokasi2){
  const sel1 = lokasi1 ? lokasi1 : "A1";
  const sel2 = lokasi2 ? lokasi2 : "A1";
  const hamparan = SpreadsheetApp.openById("spreadsheet ID");
  const lembaran1 = hamparan.getSheetByName(lemb1);
  const dataLemb1 = lembaran1.getRange(sel1).getDataRegion().getDisplayValues();
  dataLemb1.shift();

  if (lemb2){
    const lembaran2 = hamparan.getSheetByName(lemb2);
    const dataLemb2 = lembaran2.getRange(sel2).getDataRegion().getDisplayValues();
    dataLemb2.shift();
    const data = {dataLemb1: dataLemb1, dataLemb2: dataLemb2};
    return data;
  } else {
    const data = dataLemb1;
    return data;
  }
}
```

## Presenting Data in Table

```js
function binaJadualLaporan(d){
  const badanJadual = ambil("badan-jadual-laporan");

  d.forEach(b => {
    let baris = buat("tr");

    for (let i=0; i<12; i++){
      let lajur = buat("td");
      lajur.textContent = b[i];
      baris.appendChild(lajur);
    }

    badanJadual.appendChild(baris);
  });
}


function buat(e){
  return document.createElement(e);
}


function ambil(t){
  return document.getElementById(t);
}
```

## Filter Data

```js
function simpanData(dataDariGoogleSheet){
  dataPerolehanBarangan = dataDariGoogleSheet;
  ambil("pusingTunggu").classList.toggle("d-none");
  ambil("kotakSenaraiBarangan").classList.toggle("d-none");
}


function binaJadualBarangan(){
  unitTerpilih = ambil("pilihUnit").value;
  data = dataPerolehanBarangan.filter(d => {return d[2] === unitTerpilih});
  data.sort();

  const badanJadual = ambil("badan-jadual-barangan");
  const lajurTerpilih = [1, 3, 4, 5];
  
  badanJadual.innerHTML = "";

  data.forEach(b => {
    let baris = buat("tr");

    for (let i=0; i<4; i++){
      let lajur = buat("td");
      lajur.textContent = b[lajurTerpilih[i]];
      baris.appendChild(lajur);
    }

    badanJadual.appendChild(baris);
  });
}
```

Some webpage has a more detailed filter in place:

```js
function binaJadualPO(praRujUnit){
  const badanJadual = ambil("badan-jadual-po");

  badanJadual.innerHTML = "";

  let dataPOtertapis = dataPO.filter((data)=>{return data[0].startsWith(praRujUnit);});

  let templat = ambil("templatJadual").content;

  dataPOtertapis.forEach(b => {
    let baris = templat.cloneNode(true);
    let rujUnit = baris.querySelector(".rujUnit");
    let pembekal1 = baris.querySelector(".pembekal1");
    let jumlahPO = baris.querySelector(".jumlahPO");
    let nomborPO = baris.querySelector(".nomborPO");
    let statusPadanan = baris.querySelector(".statusPadanan");
    let teruskan = baris.querySelector(".butangTeruskan");
    let padanan = baris.querySelector(".butangPadanan");

    rujUnit.textContent = b[0];
    teruskan.dataset.rujUnit = b[0];
    pembekal1.textContent = b[3];
    jumlahPO.textContent = b[6];
    nomborPO.textContent = b[7];
    statusPadanan.textContent = b[10];
  
    teruskan.addEventListener("click", (e)=>{padankanPO(e);});
    padanan.addEventListener("click", (e)=>{paparkanButang(e);});
    badanJadual.appendChild(baris);
  });
}
```

# Update Data

```js
function kemaskiniPadanan(rujUnit, tarikhPadanan){
  const hamparan = SpreadsheetApp.openById("spreadsheet ID");
  const lembaran = hamparan.getSheetByName("PO");
  const dataRujUnit = lembaran.getRange(2, 1, lembaran.getLastRow() - 1, 1).getValues().map((r)=>r[0]);
  let baris = dataRujUnit.indexOf(rujUnit) + 2;
  lembaran.getRange(baris, 11).setValue("Bersih");
  lembaran.getRange(baris, 10).setValue(tarikhPadanan);
  return ambilData("PO");
}
```

## Simple Update to Data
The following code is located in their respective `js-webpage.html` file

```js
function padankanPO(e){
  let rujUnit = e.target.dataset.rujUnit;
  let tarikhPadanan = e.target.previousElementSibling.value;
  let pRU = unitTerpilih.value;
  dataPO = [];
  google.script.run.withSuccessHandler((e)=>{simpanData(e, pRU);}).kemaskiniPadanan(rujUnit, tarikhPadanan);
  suisPaparan(1000);
}
```

The corresponding code is located in the `Code.gs` file.

```js
function kemaskiniPadanan(rujUnit, tarikhPadanan){
  const hamparan = SpreadsheetApp.openById("spreadsheet ID");
  const lembaran = hamparan.getSheetByName("PO");
  const dataRujUnit = lembaran.getRange(2, 1, lembaran.getLastRow() - 1, 1).getValues().map((r)=>r[0]);
  let baris = dataRujUnit.indexOf(rujUnit) + 2;
  lembaran.getRange(baris, 11).setValue("Bersih");
  lembaran.getRange(baris, 10).setValue(tarikhPadanan);
  return ambilData("PO");
}
```

# Delete Data

```js
function padamRekod(bil, seterusnya){
  const hamparan = SpreadsheetApp.openById("spreadsheet ID");
  const lembaranPO = hamparan.getSheetByName("PO");
  const lembaranTerperinci = hamparan.getSheetByName("PO Terperinci");

  const dataBilPO = lembaranPO.getRange(1, 1, lembaranPO.getLastRow(), 1).getValues().map(r => r[0]);
  const dataBilTerperinci = lembaranTerperinci.getRange(1, 1, lembaranTerperinci.getLastRow(), 1).getValues().map(r => r[0]);

  const barisBilPO = dataBilPO.indexOf(bil) + 1;
  lembaranPO.deleteRow(barisBilPO);

  let j = dataBilTerperinci.length;
  while (dataBilTerperinci.lastIndexOf(bil, j) > 0){
    let indeks = dataBilTerperinci.lastIndexOf(bil, j);
    let baris = indeks + 1;
    lembaranTerperinci.deleteRow(baris);
    j = indeks - 1;
  }

  if (!seterusnya){
    TerikatRekodLPO.onEdit();

    const folderPDF = DriveApp.getFolderById("folder ID");
    const failLama = folderPDF.getFilesByName(bil);

    while (failLama.hasNext()){
      let failLamaIni = failLama.next();
      failLamaIni.setTrashed(true);
    }

    return ambilData("PO", "A1", "PO Terperinci", "A1");
  }

}
```

# Save Data as .pdf

```js
function cetakPO(bil){
  const namaFailGS = "sementara" + bil;
  const folderPDF = DriveApp.getFolderById("folder ID");
  const templatGS = DriveApp.getFileById("template file ID");
  const failBaru = templatGS.makeCopy(namaFailGS, folderPDF);
  const idFailBaru = failBaru.getId();

  const lembaran = SpreadsheetApp.openById(idFailBaru).getActiveSheet();

  const dataTerperinci = ambilData("PO", "A1", "PO Terperinci", "A1");
  const senaraiPembekal = dataTerperinci.dataLemb1.filter(rekod => {return rekod[0] === bil})[0];
  const dataTerpilih = dataTerperinci.dataLemb2.filter(rekod => {return rekod[0] === bil});

  lembaran.getRange("F21").setValue(dataTerpilih[0][0]);
  lembaran.getRange("A44").setValue("Pembekal-1. " + senaraiPembekal[3]);
  lembaran.getRange("A45").setValue("Pembekal-2. " + senaraiPembekal[4]);
  lembaran.getRange("A46").setValue("Pembekal-3. " + senaraiPembekal[5]);

  const jumlahRekod = dataTerpilih.length;
  for (i=0; i<jumlahRekod; i++){
    lembaran.getRange(i+5, 2).setValue(dataTerpilih[i][2]);
    lembaran.getRange(i+5, 4).setValue(dataTerpilih[i][3]);
    lembaran.getRange(i+5, 5).setValue(dataTerpilih[i][4]);
    lembaran.getRange(i+5, 6).setValue(dataTerpilih[i][5]);
  }

  SpreadsheetApp.flush();
  
  const failLama = folderPDF.getFilesByName(bil);

  while (failLama.hasNext()){
    let failLamaIni = failLama.next();
    failLamaIni.setTrashed(true);
  }

  const failPDF = failBaru.getAs("application/pdf");
  folderPDF.createFile(failPDF).setName(bil);
  failBaru.setTrashed(true);
}
```


