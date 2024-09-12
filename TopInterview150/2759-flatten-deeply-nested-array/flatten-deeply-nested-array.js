/**
 * @param {Array} arr
 * @param {number} depth
 * @return {Array}
 */
var flat = function (arr, n) {
    if(n===0){
        return arr;
    }
    let result = [];
    arr.forEach(element => {
        if (Array.isArray(element)) {
            result.push(...flat(element,n-1)) // Recursively flatten the nested array
        } else {
            result.push(element);  // Add non-array elements to the result
        }
    });
    return result;
};