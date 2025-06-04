class Solution:
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:
        if int(s) > finish:
            return 0

        answer = set()
        my_answer = set()

        # for i in range(start, finish + 1):
        #     i_str = str(i)
        #     if i_str[len(i_str) - len(s):] == s:
        #         answer.add(i_str)

        finish_digit = len(str(finish))
            
        cascading_queue = [s]
        # bfs
        count = 1 if int(s) >= start else 0
        while cascading_queue:
            # print(cascading_queue)
            node = cascading_queue.pop(0)

            if len(node) < finish_digit - 1:
                cascading_queue.append("0" + node)

            for i in range(1, (limit + 1)): # 1, 2, 3, 4
                i_str = str(i)
                next_node_str = i_str + node
                next_node_int = int(next_node_str)

                if start <= next_node_int <= finish:
                    count += 1
                    cascading_queue.append(next_node_str)
                    my_answer.add(next_node_str)
                elif next_node_int < start:
                    cascading_queue.append(next_node_str)
                    my_answer.add(next_node_str)

        print(answer - my_answer)
        print("111223" in my_answer)

        return count

s = Solution()

s.numberOfPowerfulInt(1829505, 1255574165, 7, "11223")
