from stats import get_num_words, get_char_counts, get_sorted_list
import sys

def get_book_text(path):
    with open(path) as f:
        return f.read()

def main():
    # Kiểm tra số lượng đối số
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
        
    # Lấy đường dẫn file từ đối số dòng lệnh
    book_path = sys.argv[1]
    
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    
    char_counts = get_char_counts(text)
    sorted_chars = get_sorted_list(char_counts)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    
    for item in sorted_chars:
        print(f"{item['char']}: {item['num']}")
        
    print("============= END ===============")

main()