# Trancy

k1 >> play()
k1.degree = "V="

d1 >> play()
d1.degree = "[--]"
d1.dur=0.5
d1.sample=3

d2 >> play()
d2.degree="  H "
d2.sample=0
d2.room=0.5
d2.mix=0.2

print(Samples)
Clock.clear()


k1 >> play("X ")

d1 >> play("-", dur=0.25, amp=[0,1,1,0, 0,0,1,1, 0,1,1,0, 0,0,1,0])
d2 >> play("  O ", sample=2, amp=0.2, lshift=0.1)
d3 >> play("   (= )", sample=3)


# Electro housey
