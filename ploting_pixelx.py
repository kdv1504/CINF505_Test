import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as tk

'''Multi-K for CIFAR-10'''

days = [1, 2, 3, 4, 5, 6, 10, 14, 15, 21, 29]
t_acc = [0.9062677621040666, 0.8939699271430785, 0.8899395442567044, 0.8860125045212629, 0.8820854647858213, 0.8771766651165194, 0.8790368418333075, 0.8726812380509482, 0.8717511496925541, 0.862656952410479, 0.8374412235829071]
t_f1 = [0.865170209603092, 0.8483594442802247, 0.8432671081677704, 0.8378418112319906, 0.8321318228630278, 0.825413147264047, 0.8279561990152128, 0.8195929125787085, 0.8184610883557636, 0.8065502183406114, 0.7726878612716763]
v_acc =[0.8726790450928382,0.8594164456233422, 0.8474801061007957, 0.8417329796640142, 0.8359858532272325, 0.8355437665782494]
v_f1 =[0.8132295719844358, 0.7979669631512071, 0.7806738715829625, 0.7713920817369093, 0.7635436583811345, 0.7642585551330798]
test_acc = [0.8565863160457755, 0.8361334307280254, 0.8263939615290966, 0.8132456781105429, 0.8100803506208911, 0.8054541027514001, 0.7949841733625518, 0.7974190406622839, 0.796445093742391, 0.7888970051132214, 0.7713659605551497]
test_f1 = [0.7844859129162093, 0.7610933617323393, 0.7504375218760938, 0.7304042179261863, 0.7245762711864406, 0.7195507195507196, 0.702893436838391, 0.7094972067039106, 0.7105263157894737, 0.6986444212721585, 0.6800681431005111]

# 10 days: t_acc: 0.8790368418333075, t_f1: 0.8279561990152128, test_acc: 0.7949841733625518, test_f1: 0.702893436838391
# 14 days: t_acc: 0.8708727329096264, t_f1: 0.8172577696526508, test_acc: 0.7935232529827124, test_f1: 0.7030812324929971


fig, ax = plt.subplots()
plt.figure(figsize=(15, 6), dpi=100)
plt.plot(t_acc, color= 'b', linestyle='-', marker='>', markeredgewidth=4,linewidth=3,label="Train Acc")
plt.plot(test_acc, color= 'r', linestyle=':', marker='>', markeredgewidth=4,linewidth=3,label="Test Acc")
plt.plot(t_f1, color= 'g', linestyle='-', marker='d', markeredgewidth=4,linewidth=3,label="Train F1")
plt.plot(test_f1, color= 'c', linestyle='-.', marker='s', markeredgewidth=4,linewidth=3, label="Test F1")

plt.legend( fontsize=20 )
# plt.legend(bbox_to_anchor=(1.01, 1.01), borderaxespad=0., fontsize=13)

# plt.xlim([0, 505])
positions = (0,1, 2, 3,4, 5, 6, 7, 8, 9, 10)
labels = ("1", "2","3", "4", "5", "6", "10", "14", "15", "21", "29")
plt.ylim([0, 1]) # 4.45 3.45
# plt.xticks(b, fontsize=16)
# ax.set_xticks(b)
# ax.get_xaxis().set_major_formatter(tk.ScalarFormatter())
plt.xticks(positions, labels, fontsize=20)
# plt.xticks(fontsize=16)
plt.yticks(fontsize=20 )
plt.ylabel('Metrics', fontsize=20)
plt.xlabel('Lead time (days)',  fontsize=20)
plt.savefig('wildfire.png', bbox_inches = "tight")

exit()

'''Different values of beta for CIFAR-10'''

b = [1,5,10,100]
a1 = [10.30,31.42,42.58,77.44]
a5 = [27.14,32.04,46.46,74.06]
a10 = [41.23,44.19,45.75,70.33]
a100 = [79.62,76.57,74.57,76.07]
a2 = [28.87,28.87,28.87,28.87]

fig, ax = plt.subplots()
plt.plot(a2, color= 'm', linestyle=':', marker='*', markeredgewidth=4,linewidth=3, label="EG-Booster")
plt.plot(a1, color= 'g', linestyle='-.', marker='d', markeredgewidth=4,linewidth=3, label="$\\alpha$ = 1")
plt.plot(a5, color= 'b', linestyle='--', marker='>', markeredgewidth=4,linewidth=3, label="$\\alpha$ = 5")
plt.plot(a10, color= 'c', linestyle=':', marker='<', markeredgewidth=4,linewidth=3, label="$\\alpha$ = 10")
plt.plot(a100, color= 'r', linestyle='-', marker='s', markeredgewidth=6,linewidth=3, label="$\\alpha$ = 100")
# plt.legend( fontsize=20 )
plt.legend(loc='lower right', fontsize=18, framealpha=0.5 )
# plt.legend(bbox_to_anchor=(1.01, 1.01), borderaxespad=0., fontsize=13)

# plt.xlim([0, 505])
positions = (0,1, 2, 3)
labels = ("1", "5","10", "100")
plt.ylim([5, 85 ]) # 4.45 3.45
# plt.xticks(b, fontsize=16)
# ax.set_xticks(b)
# ax.get_xaxis().set_major_formatter(tk.ScalarFormatter())
plt.xticks(positions, labels, fontsize=20)
# plt.xticks(fontsize=16)
plt.yticks(fontsize=20 )
plt.ylabel('Attack SR', fontsize=20)
plt.xlabel('$\\beta$',  fontsize=20)
plt.savefig('attacksr.png', bbox_inches = "tight")

'''Multi-K for Imagenette'''
k = [1, 5, 30,60,90,120]
a1 = [10.30,61.08,77.44,83.24,84.18]
a2 = [27.42,75.44,88.78,91.32,90.86]
a3 = [30.42,87.01,94.76,96.01,94.86]

# a2 = [28.87,28.87,28.87,28.87,28.87]
# a5 = [27.14,32.04,46.46,74.06]
# a10 = [41.23,44.19,45.75,70.33]
# a100 = [79.62,76.57,74.57,76.07]
fig, ax = plt.subplots()
plt.plot(a1, color= 'b', linestyle='--', marker='>', markeredgewidth=4,linewidth=3,label="$\\beta=1$")
plt.plot(a2, color= 'g', linestyle='-.', marker='d', markeredgewidth=4,linewidth=3,label="$\\beta=2$")
plt.plot(a3, color= 'r', linestyle='-', marker='s', markeredgewidth=4,linewidth=3,label="$\\beta=3$")

plt.legend( fontsize=20 )
# plt.legend(bbox_to_anchor=(1.01, 1.01), borderaxespad=0., fontsize=13)

# plt.xlim([0, 505])
positions = (0,1, 2, 3,4)
labels = ("1", "30","60", "90", "120")
plt.ylim([5, 100 ]) # 4.45 3.45
# plt.xticks(b, fontsize=16)
# ax.set_xticks(b)
# ax.get_xaxis().set_major_formatter(tk.ScalarFormatter())
plt.xticks(positions, labels, fontsize=20)
# plt.xticks(fontsize=16)
plt.yticks(fontsize=20 )
plt.ylabel('Attack SR', fontsize=20)
plt.xlabel('$K$',  fontsize=20)
plt.savefig('attacksr_k.png', bbox_inches = "tight")
