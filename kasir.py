import makanan as pesan
import pembayaran as bayar
import pelanggan as customer

pesanan = []
total = []

print('Selamat Datang di Cibiuk')
print('---------Menu-----------')
print('1. Rendang     Rp. 20000')
print('2. Soto        Rp. 25000')
print('3. Seblak      Rp. 30000')

member = input('Apakah kamu memiliki member? (y/n)  ')
match member:
    case 'y':
        customer.member = True
    case 'n':
        customer.member = False
    case other:
        customer.member = False

while True:
    pilihan = input('Masukan pilihan kamu: ')
    if pilihan == '1' and member == 'n':
        pesan.menu = 'Daging'
        pesan.harga = int(20000)
    elif pilihan == '2' and member == 'n':
        pesan.menu = 'Soto'
        pesan.harga = int(25000)
    elif pilihan == '3' and member == 'n':
        pesan.menu = 'Rendang'
        pesan.harga = int(25000)
    elif pilihan == '1' and member == 'y':
        pesan.menu = 'Daging'
        pesan.harga = 10000
    elif pilihan == '2' and member == 'y':
        pesan.menu = 'Soto'
        pesan.harga = 20000
    elif pilihan == '3' and member == 'y':
        pesan.menu = 'Rendang'
        pesan.harga = 25000
    else:
        pesan.menu = 'null'
        pesan.harga = 0
        break

    pesanan.append(pesan.menu)
    memesan = input('Pesan lagi ? (y/n)')
    match memesan:
        case 'n':
            total.append(int(pesan.harga))
            break
        case 'y':
            total.append(int(pesan.harga))
        case other:
            print('error invalid')

uang = input('Masukan jumlah uang yang dibayarkan')

customer.uang = int(uang)
customer.total = bayar.arraysum(total)

if int(customer.uang) >= int(customer.total):
    print('-------struk-------')
    print('barang yang dipesan')
    print(pesanan)
    print('Status member')
    print()
    print('Uang yang dibayarkan')
    print(customer.uang)
    print('Total Harga')
    print(bayar.arraysum(total))
    print('Kembalian')
    print(customer.kembalian(customer.uang, bayar.arraysum(total)))
else:
    print('-------struk-------')
    print('barang yang dipesan')
    print(pesanan)
    print('Status member')
    print()
    print('Uang yang dibayarkan')
    print(customer.uang)
    print('Total Harga')
    print(bayar.arraysum(total))
    print('Uang mu tidak cukup')
    print('pembayaran dibatalkan')
