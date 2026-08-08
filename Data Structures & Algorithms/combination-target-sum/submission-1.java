class Solution {
    public List<List<Integer>> combinationSum(int[] nums, int target) {
        List<List<Integer>> res = new ArrayList<>();
        List<Integer> subset = new ArrayList<>();
        backtrack(nums,subset,0,res,target);
        return res;
    }

    private void backtrack(int[] nums, List<Integer> subset,int sum, List<List<Integer>> res, int target)
    {
        if(sum==target)
        {
            res.add(new ArrayList<>(subset));
            return;
        }

        if(sum>target)
        {
            return;
        }

        for(int num: nums)
        {
            if(!subset.isEmpty() && num < subset.get( subset.size() - 1))
                continue;
            subset.add(num);
            backtrack(nums,subset,sum+num,res,target);
            subset.remove(subset.size()-1);
        }
    }
}
