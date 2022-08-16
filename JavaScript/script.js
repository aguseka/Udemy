js = "amazing";
console.log(10+20+30+40+50);
console.log("Agus Eka Maharta");

const firstName = "Eka";
console.log(firstName)
const weightEka = 90;
const heightEka = 1.69;
const weightSatria = 80;
const heightSatria = 1.69;
const satriaBMI = weightSatria/(heightSatria*heightSatria);
const ekaBMI = weightEka/(heightEka*heightEka);

console.log(`BMI Eka ${ekaBMI}`)
console.log(`BMI Satria ${satriaBMI}`)
if(satriaBMI>ekaBMI){console.log(`Nilai BMI Satria lebih besari dari Eka senilai ${satriaBMI}`)}
else if (satriaBMI===ekaBMI){console.log(`Nilai BMI Satria sama dengan BMI Eka`)}
else{console.log(`Nilai BMI Eka lebih besar dari Satria sebesar ${ekaBMI}`)}


/*let 
let licenseAge = 18
let satriaAge = 20

if(satriaAge>=licenseAge) {console.log(' Anak ini sudah bisa mengurus SIM')}
else {console.log(`Anak ini perlu ${licenseAge-satriaAge} tahun lagi sebelum boleh mimiliki SIM`)}
*/