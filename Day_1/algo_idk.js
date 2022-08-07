
const keys1 = ["abc", 3, "yo"];
const vals1 = [42, "wassup", true];
const expected1 = {
    abc: 42,
    3: "wassup",
    yo: true,
};

const keys2 = [];
const vals2 = [];
const expected2 = {};

// Bonus
const bonus_keys1 = [["abc", "def"], 3, "yo"];
const bonus_vals1 = [42, "wassup", true];
const bonus_expected1 = {
    abc: 42,
    def: 42,
    3: "wassup",
    yo: true,
};

const bonus_keys2 = ["abc", 3, "yo", 'something'];
const bonus_vals2 = [42, "wassup", true];
const bonus_expected2 = {
    abc: 42,
    3: "wassup",
    yo: true,
  something: null // undefined
};

// **posibility
// const bonus_keys3 = ["abc", 3, "yo"];
// const bonus_vals3 = [42, "wassup", true, 'something'];
// const bonus_expected3 = {
//   abc: 42,
//   3: "wassup",
//   yo: true,
//   something : 'something'
// };

const bonus_keys3 = ["abc", 3, "yo"];
const bonus_vals3 = [42, "wassup", true, 'something'];
const bonus_expected3 = False


/**
 * Converts the given arrays of keys and values into an object.
 * - Time: O(?).
 * - Space: O(?).
 * @param {Array<string>} keys
 * @param {Array<any>} values
 * @returns {Object} The object with the given keys and values.
 */
function zipArraysIntoMap(keys, values) {
    dictionary = dict(zip(keys, values))
}
return dictionary