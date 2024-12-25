import re

def split_into_sliding_window_chunks(text: str, window_size: int = 3) -> list:
    sentences = re.split(r'(?<=[.!?])\s+', text)
    chunks = []
    for i in range(len(sentences) - window_size + 1):
        chunk = " ".join(sentences[i:i + window_size])
        chunks.append(chunk)
    return chunks


text = "ОБЩЕСТВО С ОГРАНИЧЕННОЙ ОТВЕТСТВЕННОСТЬЮ «Лоция»  121351, Москва г., Партизанская ул., дом 25, ЭТ 5 ПОМ I КОМ 15  ИНН 9731028047 / КПП 773101001 ОГРН 1197746102388    ПРИКАЗ г. Москва  05.07.2021 г.              № 104/21-О  Об утверждении Методики  календарно-сетевого планирования  при реализации проектов  В целях совершенствования процессов календарно-сетевого планирования в ООО «Лоция»:   ПРИКАЗЫВАЮ:  1. Утвердить Методику календарно-сетевого планирования при реализации проектов (далее – Методика) в соответствии с приложением № 1 к настоящему приказу. 2. Ввести в действие Положение с 05.07.2021г. 3. Руководителям структурных подразделений организовать изучение Положения подчиненными работниками в части, их касающейся, и обеспечить выполнение изложенных в Положении требований. 4. Контроль за исполнением настоящего приказа оставляю за собой.  Генеральный директор        И.В. Гапонов    "
chunks = split_into_sliding_window_chunks(text)
print(chunks[0])
print(chunks[1])