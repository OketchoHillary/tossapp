import uuid


x = uuid.uuid4().hex[:8].upper()
print x

newF = f.save()
while True:
    key = make_key()
    if not Thing.objects.filter(key=key).exists():
        break
newF.key = key
newF.save()