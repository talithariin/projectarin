# Fungsi simpan dalam perangkat
def save():
    if textStruk.get(1.0, END) == '\n':
        pass
    else:
        # Tentukan path file
        file_path = r'C:\Users\syari\Document\KULIAH\Semester 5\Pemlan\Praktikum\projek\ReceiptHistory.csv'

        bill_data = textStruk.get(1.0, END)

        # Write the data in CSV format
        with open(file_path, 'a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

            # Split the data into lines and write each line as a row
            for line in bill_data.split('\n'):
                writer.writerow([line])

        messagebox.showinfo('Information', 'Your receipt has been saved')
# Batas fungsi simpan dalam perangkat
