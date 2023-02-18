/**
 * @param {number[]} nums
 * @return {number[]}
 */
var getConcatenation = function(nums) {
    let res = nums;
    nums.forEach((i)=>{
       res.push(i);
    });
    return res;
};