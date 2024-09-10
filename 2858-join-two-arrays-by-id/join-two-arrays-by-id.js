/**
 * @param {Array} arr1
 * @param {Array} arr2
 * @return {Array}
 */
var join = function(arr1, arr2) {
    var ans = {};
    
    for (var i = 0; i < arr1.length; i++) {
        ans[arr1[i].id] = arr1[i];
    }

    for (var i = 0; i < arr2.length; i++) {
        var currId = arr2[i].id; 
        
        if (currId in ans) {
            var currVal = arr2[i];
            for (const [key, value] of Object.entries(currVal)) {
                ans[currId][key] = value;
            }
        } else {
            ans[currId] = arr2[i];
        }
    }
    return Object.values(ans);
};