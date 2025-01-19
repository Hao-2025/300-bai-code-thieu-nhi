#Đề bài
#Cho một danh sách các số nguyên "nums" và một số nguyên "target".
#Yêu cầu cần tìm trong danh sách số nums sao cho tổng của chúng bằng số target.
#Sau đó trả ra số chỉ của 2 số đó.
#Ví dụ:
# Input
# nums = [2,7,11,15] target = 9
# Output
# [0,1] 

#Two sum
# Cách tiếp cận bài toán (đơn giản)
# 1. Duyệt qua các cặp phần tử trong danh sách
# 2. Kiểm tra xem tổng các cặp số có bằng target không
# 3. Nếu có, trả về chỉ số của cặp số đó


def twoSum(nums, target):
  # Duyệt qua các phần tử trong danh sách nums
      for i in range(nums):
        for j in range(i + 1, len(nums)):
            # Kiểm tra xem tổng của nums[i] và nums[j] có bằng target không
            if nums[i] + nums[j] == target:
                return [i, j] # Trả về chỉ số của 2 số có tổng bằng target
      return None # Không tìm thấy cặp nào thì trả về None
 

