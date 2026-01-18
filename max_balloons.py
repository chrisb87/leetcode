# Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.
# You can use each character in text at most once. Return the maximum number of instances that can be formed.

from collections import defaultdict


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        target = "balloon"
        target_count = defaultdict(int)
        for letter in target:
            target_count[letter] += 1

        answer = 0

        current_count = defaultdict(int)
        for letter in text:
            current_count[letter] += 1
            found_word = True

            for target_letter, target_letter_count in target_count.items():
                if current_count[target_letter] < target_letter_count:
                    found_word = False
                    break
            
            if found_word:
                answer += 1
                for target_letter, target_letter_count in target_count.items():
                    current_count[target_letter] -= target_letter_count

        return answer


def test_example_1():
    text = "nlaebolko"
    assert Solution().maxNumberOfBalloons(text) == 1

def test_example_2():
    text = "loonbalxballpoon"
    assert Solution().maxNumberOfBalloons(text) == 2

def test_example_3():
    text = "leetcode"
    assert Solution().maxNumberOfBalloons(text) == 0

def test_failure_1():
    text = "krhizmmgmcrecekgyljqkldocicziihtgpqwbticmvuyznragqoyrukzopfmjhjjxemsxmrsxuqmnkrzhgvtgdgtykhcglurvppvcwhrhrjoislonvvglhdciilduvuiebmffaagxerjeewmtcwmhmtwlxtvlbocczlrppmpjbpnifqtlninyzjtmazxdbzwxthpvrfulvrspycqcghuopjirzoeuqhetnbrcdakilzmklxwudxxhwilasbjjhhfgghogqoofsufysmcqeilaivtmfziumjloewbkjvaahsaaggteppqyuoylgpbdwqubaalfwcqrjeycjbbpifjbpigjdnnswocusuprydgrtxuaojeriigwumlovafxnpibjopjfqzrwemoinmptxddgcszmfprdrichjeqcvikynzigleaajcysusqasqadjemgnyvmzmbcfrttrzonwafrnedglhpudovigwvpimttiketopkvqw"
    assert Solution().maxNumberOfBalloons(text) == 10
