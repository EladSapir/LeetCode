/**
 * @param {Function[]} functions
 * @return {Function}
 */
var compose = function(functions) {
    if(functions.length===0){
        return function(x){ return x;};
    }
    else{
        return function(x) {
            let i=functions.length-1;
            let func=x;
            while (i!=-1){
                func=functions[i](func);
                i--;
            }
            return func;
        }
    }
    
};

/**
 * const fn = compose([x => x + 1, x => 2 * x])
 * fn(4) // 9
 */