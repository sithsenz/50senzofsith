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
These 2 functions have to go hand in hand.

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

## Create New Data

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

## Read Data

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

## Update Data

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

## Delete Data

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

## Save Data as .pdf

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

## JS Codes Specific to Each .html File
Each webpage usually starts with reading data from specified range after a successful `DOMContentLoaded` event.

```js
document.addEventListener('DOMContentLoaded', ()=>{
  google.script.run.withSuccessHandler(binaJadualLaporan).ambilData("Laporan");
});
```

### Presenting Data in Table

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

### Filter Data

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

### Simple Update to Data
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

