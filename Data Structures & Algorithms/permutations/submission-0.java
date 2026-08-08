class Solution {
    public List<List<Integer>> permute(int[] nums) {
        List<List<Integer>> res = new ArrayList<>();
        List<Integer> subset = new ArrayList<>();
        backtrack(nums,subset,res);
        return res;
    }

    private void backtrack(int[] nums, List<Integer> subset, List<List<Integer>> res)
    {
        if(subset.size()==nums.length)
        {
            res.add(new ArrayList<>(subset));
            return;
        }

        for(int num: nums)
        {
            if (subset.contains(num))
                continue;
            subset.add(num);
            backtrack(nums,subset,res);
            subset.remove(subset.size()-1);
        }
    }
}
