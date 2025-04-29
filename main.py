from parser import * 
from utils import * 

def preprocess(list_of_numbers):
    number_in_text = filter_above(list_of_numbers, target_number)
    number_in_text.sort()
    return number_in_text

def run(number_in_text, target_number, output_file_name = DEFAULT_OUTPUT_FILE_PATH):
    with open('output.txt', 'w', encoding='utf-8') as out:
        for k in list_ks:
            print(f'Ava is processing the document...🔮, assuming the possible sum of {k} numbers')
            result = find_k_sum_backtrack(number_in_text, target_number, k)
            output_txt = f'k={k} → {len(result)} combinations\n'
            out.write(output_txt)
            print(f'Ava found this with k = {k} \n')
            print(output_txt)
            # write each tuple on its own line
            for comb in result:
                output_txt = '  ' + ','.join(map(str, comb)) + '\n'
                print(output_txt)
                out.write(output_txt)

            out.write('\n')  # blank line between different k

if __name__== '__main__':
    print('Welcome to your document parser! \n')
    target_number = TARGET_NUMBER
    print(f'The target number is {target_number}')
    number_in_text = extract_dollar_values(allow_duplicates = True)
    number_in_text = preprocess(number_in_text)
    list_ks = list(range(MIN_K, MAX_K+1))
    run(number_in_text = number_in_text, target_number = target_number)

    