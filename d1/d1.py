

if __name__ == "main":
    print("q234")



def day1() -> str:
    left_list: list[int] = []
    right_list: list[int] = []

    for line in get_next_line("input.txt"):
        left_list.append(line.split('\t')[0])
        right_list.append(line.split('\t')[1])



    for left_num in left_list:
        for right_num in right_list:
            
            print("")
    
        
    
def get_next_line(file_path: str):
    with open(file_path, "r") as file:
        for line in file:
            yield line
            

