var TimeLimitedCache = function() {
    this.keymap = {};
    this.activeKeysCounter  = 0;
};

/** 
 * @param {number} key
 * @param {number} value
 * @param {number} duration time until expiration in ms
 * @return {boolean} if un-expired key already existed
 */
TimeLimitedCache.prototype.set = function(key, value, duration) {
    var keyval = this.keymap[key];//if already in
    keyval ? clearTimeout(keyval.timeout) : this.activeKeysCounter ++;

    this.keymap[key] = {
        value: value,
        timeout: setTimeout(() => {
            this.keymap[key].value = -1;
            this.activeKeysCounter--;
            }, duration),
    }
    return Boolean(keyval);
};

/** 
 * @param {number} key
 * @return {number} value associated with key
 */
TimeLimitedCache.prototype.get = function(key) {
    return this.keymap[key]?.value || -1;
};

/** 
 * @return {number} count of non-expired keys
 */
TimeLimitedCache.prototype.count = function() {
    return this.activeKeysCounter;
};

/**
 * const timeLimitedCache = new TimeLimitedCache()
 * timeLimitedCache.set(1, 42, 1000); // false
 * timeLimitedCache.get(1) // 42
 * timeLimitedCache.count() // 1
 */