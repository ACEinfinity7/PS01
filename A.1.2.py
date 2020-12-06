def make_add_table(size):
    #empty table
    table = []

    #iterate through rows and columns
    for i in range(2**size):
        table_row = []
        for j in range(2**size):
            #sum current row and col value
            sum = i+j

            #blank output
            num = ""

            #break decimal number down and build up num variable with
            #binary digits
            while sum > 0:
                val = sum & 1
                num = str(val) + num
                sum = sum >> 1

            #zero pad to bit size
            while len(num) < size:
                num = "0" + num

            table_row.append(num[-size:])

        table.append(table_row)

    return table


table = make_add_table(4)
for i in table:
    print(i)
print('h')
print(table[11][7])
print(table[4][3])










                #
                # remainder = sum % 2
                # print(sum, remainder)
                # num = str(remainder) + num
                # sum = sum // 2


    # add_table = []
    #
    #
    # for i in range(2**size-1):
    #     table_row = []
    #     for j in range(2**size-1):
    #         sum = i+j
    #         out = ""
    #         print(sum)
    #         if sum == 0:
    #             pass
    #
    #         else:
    #             while sum != 0:
    #                 rem = sum & 0b0001
    #                 out += str(rem)
    #                 sum >> 1
    #                 print(sum)
    #
    #         #while len(out) < size:
    #         #    out = "0" + out
    #         table_row.append(sum)
    #
    #     add_table.append(table_row)
    #
    # return add_table




# bits = 4
# addition_table = []
#
# for i in range((2**bits)):
#     table_row = []
#     for j in range((2**bits)):
#         table_row.append(format(i+j,f'0{bits}b')[-bits:])
#     addition_table.append(table_row)
#
# for row in addition_table:
#     print(row)
#
# print(len(addition_table),len(addition_table[0]))
