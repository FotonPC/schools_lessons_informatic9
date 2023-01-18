import tkinter as tk_main
from tkinter import ttk as tk
from tkinter import messagebox as mbx

ns = "NOP SOH STX ETX EOT ENQ ACK BEL BS TAB LF VT FF CR SO SI DLE DC1 DC2 DC3 DC4 NAK SYN ETB CAN EM SUB ESC FS GS RS US SP".split()
names = {}


def names2(n):
    if n < len(ns):
        # print("gg")
        return ns[n]

    else:
        return chr(n)


for i in range(len(ns)):
    names[i] = f'{ns[i]}'


class Edit(tk_main.Text):
    def __init__(self, master, base, width=40):
        super().__init__(master, width=width, height=1 if base != 256 else 4)
        self.base = base
        self.keys = {}
        self.bases = []
        self.edits = []
        self.w = width
        self.bind("<Key>", self.handler)
        self.bind("<KeyPress>", self.handler)
        self.bind("<KeyRelease>", self.handler)
        self.tag_configure("special", background='yellow')

    def add(self, edits, bases):
        self.bases = bases.copy()
        self.bases.remove(self.base)
        self.edits = edits.copy()
        self.edits.remove(self)
        for i in range(len(bases)):
            self.keys[bases[i]] = edits[i]

    def handler(self, e=None):
        self.master.update()
        # print("handled")
        if self.base != 256:
            if 1:
                # try:
                txt = self.get("1.0", tk_main.END).replace(" ", "").replace("\n", "")
                txts = [convert_base(txt, to_base=self.bases[i], from_base=self.base)
                        for i in range(len(self.bases))]
                w = max(len(txt), max(*list(map(lambda val: len(''.join(val)), txts)), self.w))
                for e in edits:
                    e.config(width=w)
                self.config(width=w)
                for i in range(len(txts)):
                    if self.edits[i].base != 256:
                        set_text(self.edits[i], format_out(''.join(txts[i]), self.edits[i].base))
                    else:
                        ed = self.edits[i]
                        ed.delete(1.0, 'end')
                        for ch in txts[i]:
                            if len(ch) > 1:
                                # ed.insert('end', ch, 'special')
                                def show_code(e=None, code=ns.index(ch), char=ch):
                                    mbx.showinfo(title="Символ", message=f"Код {code}\nОбозначение {char}")

                                btn = tk.Button(ed, text=ch, width=4, style='SPECIAL.TButton', command=show_code)
                                ed.window_create('end', window=btn)
                            else:
                                ed.insert("end", ch)

                set_text(self, format_out(txt, self.base))
            # print("completed")
            # except Exception as error:
            #    print(error)


def convert_base(num, to_base=10, from_base=10):
    n = int(num, from_base) if isinstance(num, str) else num
    alphabet = [names2(i) for i in range(256)] if to_base == 256 else "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    res = []
    while n > 0:
        n, m = divmod(n, to_base)
        res += [alphabet[m]]
    return res[::-1]


def set_text(entry, text):
    if type(entry) == Edit:
        entry.delete('1.0', tk_main.END)
        entry.insert(1.0, text)
    else:
        entry.delete(0, tk_main.END)
        entry.insert(0, text)


def format_out(s, base=10):
    res = ""
    if base == 2:
        if len(s) > 4:
            while len(s) > 4:
                res = s[-4::] + ' ' + res
                s = s[:-4:]
            res = s + ' ' + res
            # res = res[:-2:]
        else:
            res = s
    elif base == 10:
        if len(s) > 3:
            while len(s) > 3:
                res = s[-3::] + ' ' + res
                s = s[:-3:]
            res = s + ' ' + res
            # res = res[:-2:]
        else:
            res = s
    elif base == 16:
        if len(s) > 2:
            while len(s) > 2:
                res = s[-2::] + ' ' + res
                s = s[:-2:]
            res = s + ' ' + res
            # res = res[:-2:]
        else:
            res = s
    else:
        res = s
    return res.strip()


window = tk_main.Tk()
window.title("Trojans in Delphi 7 IDE")
style = tk.Style()
style.theme_use("vista")
style.configure('SPECIAL.TButton', background='#FF8800', foreground="#FF0000", selectbackground='red',
                fieldbackground='red')
bss = []


def get_bss(e=None):
    global bss
    try:
        global l
        l = tk.Label(window, text="Введите основания через пробел")
        l.grid(column=0, row=0)

        global first
        first = tk.Entry(window, width=75)
        first.grid(column=0, row=1)

        set_text(first, "2 8 10 16")
        global run
        run = True

        def some(e=None):
            global run
            run = False

        first.bind("<Return>", some)
        while run:
            window.update()
        l.grid_remove()
        first.grid_remove()
        bss = list(map(int, first.get().split()))
        bss.sort()

    except Exception as error:
        print(error)
        get_bss()


get_bss()
edits = []
for i in range(len(bss)):
    tk.Label(window, text=str(bss[i]) + ": ").grid(row=i, column=0)
    edits.append(Edit(window, bss[i], width=70))
    edits[-1].grid(column=1, row=i)
for e in edits:
    e.add(edits, bss)

# window.resizable(False, False)
window.mainloop()
