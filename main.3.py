list, list2 = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов'], []
list = ''.join(list)
list2.extend(list)
list2.insert(1, ' "'), list2.insert(2, '0'), list2.insert(4, '" '), list2.insert(10, ' "'), list2.insert(13, '" '),
list2.insert(19, ' '), list2.insert(31, ' '), list2.insert(39, ' '), list2.insert(44, ' '), list2.insert(45, ' "'),
list2.insert(47, '0'), list2.insert(49, '" ')
print(''.join(list2))