# Məlumat strukturları və alqoritmlər

**Tələbə — Nicat Süleymanlı**

Python konsol proqramı 9 məlumat strukturunun işini və onların gündəlik istifadə nümunələrini göstərir.

## İşə salmaq

ZIP faylını açın və terminalda `DSA-Nicat` qovluğuna keçin. Python 3.12 və ya daha yeni versiya kifayətdir.

```powershell
python main.py
```

Testləri ayrıca işə salın.

```powershell
python test_structures.py
```

## Fayllar

| Fayl | Məzmun |
| --- | --- |
| `main.py` | Əsas menyu, praktik nümunələr və vaxt ölçmələri |
| `CustomDataStructures/CustomArray.py` | Sabit və dinamik massiv. Sabit massiv dolduqda xəta verir. Dinamik massiv dolduqda böyüyür, doluluq dörddə birə düşəndə kiçilir. |
| `CustomDataStructures/CustomLinkedList.py` | Tək və iki istiqamətli əlaqəli siyahılar. İkinci növdə son elementə birbaşa çatmaq olur. |
| `CustomDataStructures/SQDQ.py` | Stack, Queue və Deque. Stack son əlavə olunanı, Queue ilk əlavə olunanı çıxarır. Deque hər iki ucdan işləyir. |
| `CustomDataStructures/CustomHashTable.py` | Hash cədvəli. Eyni xanaya düşən açarlar bir siyahıda saxlanır. Cədvəl dolduqca xanaların sayı avtomatik artır. |
| `CustomDataStructures/CustomBST.py` | İkili axtarış ağacı. Əlavə etmə, axtarış, silmə, sıralı keçid və hündürlük hesablanması. |
| `test_structures.py` | Əsas əməliyyatlar və sərhəd halları üçün avtomatik testlər |

## Praktik nümunələr

- **Mətni geri al və bərpa et.** İki Stack mətnin əvvəlki və geri alınmış vəziyyətlərini saxlayır.
- **Çap növbəsi.** Queue sənədləri daxil edilmə ardıcıllığı ilə çıxarır.
- **Son 5 səhifə.** Deque dolduqda ən köhnə səhifəni silir və yeni səhifəni sona əlavə edir.

## Performans müqayisəsi

Proqram 100, 1 000 və 10 000 element üzərində vaxtı ölçür. Massivlər və əlaqəli siyahılar üçün başlanğıca əlavə etmə ilə onu geri silmə birlikdə ölçülür. Stack, Queue və Deque üçün bir əlavə və bir çıxarma birlikdə ölçülür. Hash cədvəli massivdə xətti axtarışla müqayisə edilir. BST üçün qarışıq və artan giriş sıralarında qurulma vaxtı və ağacın hündürlüyü göstərilir.

| Əməliyyat | Vaxt mürəkkəbliyi |
| --- | --- |
| Massivdə indekslə oxuma | O(1) |
| Massivdə əvvələ əlavə etmə və ya əvvəldən silmə | O(n) |
| Massivdə və əlaqəli siyahıda axtarış | O(n) |
| Stack-ə əlavə etmə və çıxarma | Amortizasiya olunmuş O(1) |
| Queue və Deque-də ucdan işləmə | O(1) |
| Hash cədvəlində axtarış | Orta O(1), ən pis halda O(n) |
| BST-də axtarış | O(h), burada h ağacın hündürlüyüdür |
