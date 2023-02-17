/**
 * @param {number} num
 * @return {number}
 */
var minimumSum = function(num) {
    const myFunc = num => num;
    const a = Array.from(String(num), myFunc).sort();
    
    return parseInt(a[0]+a[2])+parseInt(a[1]+a[3]);
};