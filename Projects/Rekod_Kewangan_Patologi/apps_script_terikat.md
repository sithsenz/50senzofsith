## Custom Functions
### onEdit()
Function is run when changes to the content of the spreadsheet are detected.
Does not seem to be triggered when editing the spreadsheet directly with GSheets.
`setValue()` is used to input value into a cell, can be used to input formula as well.

### namakanKawasan()
Name a range of cells in the spreadsheet. `getDataRegion()` is similar to pressing `Ctrl A` and will select the range of cells linked to the current cell.

```js
function namakanKawasan(lemb, selMula, namaKawasan){
  let kawasan = lemb.getRange(selMula).getDataRegion();
  hamparan.setNamedRange(namaKawasan, kawasan);
}
```

### namakanLajur()
Similar to `namakanKawasan()` but will only name the selected column(s).

```js
function namakanLajur(lemb, barisMula, lajurMula, jumlahLajur, namaLajur){
  let jumlahBaris = lemb.getRange(barisMula, lajurMula).getDataRegion().getLastRow() - 1;
  let lajur = lemb.getRange(barisMula, lajurMula, jumlahBaris, jumlahLajur);
  hamparan.setNamedRange(namaLajur, lajur);
}
```

### salinFormula()
Copy the formula from `kawasanAsal` to (`barisMula`, `lajurMula`).

```js
function salinFormula(lemb, kawasanAsal, barisMula, lajurMula, jumlahLajur){
  let asal = lemb.getRange(kawasanAsal);
  let jumlahBaris = lemb.getRange(barisMula, lajurMula).getDataRegion().getLastRow() - 1;
  let destinasi = lemb.getRange(barisMula, lajurMula, jumlahBaris, jumlahLajur);
  asal.copyTo(destinasi);
}
```
