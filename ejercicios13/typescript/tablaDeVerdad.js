let v1 = false;
let v2 = true;

for (let i = 0; i < 4; i++) {
    let vf = (v1 != v2);
    document.write(`-----${vf} <br> `);
        if (i % 2 ===0) {
            v1=!v1
        }
}