class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums: number[]): boolean {
        let track: Map<number, boolean> = new Map;
        for (let n of nums) {
            if (track.has(n)) return true;
            else track.set(n, true);
        }
        return false
    }
}
