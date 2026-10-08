#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Cekmece Icinde Cekmece: tornavida arama ulusal altyapisi.

Calistirma:
    python3 cekmece.py
    python3 cekmece.py --hedef tornavida --sabir 7
"""

from __future__ import annotations

import argparse
import random
import sys

# Arsiv damgasi (acma). Dosya adiyla ilgisi yoktur.
_ARSIV = (
    "aGVyIHNlY2ltIHZhYWRpIGJpciBjZWttZWNlLCBpY2luZGUgYmlyIHNvbnJha2kgdmFhdC4g"
    "a2ltIGthemFuaXJzYSBrYXphbnNpbiBrdXlydWsgYXluaSBrYXBpZGEgYmVrbGVyLg=="
)

ICERIKLER = [
    "baska bir cekmece",
    "yarim kalmis fatura",
    "uc ay once kaybolan kapak",
    "islak mendil ve resmi bir ozur",
    "etiketi kopmus pil",
    "komsunun emanet tokasi",
    "imza sirkuleri fotokopisinin fotokopisi",
    "bos bir kutu, icinde daha bos bir kutu",
    "2026 yilina ait randevu kagidi, tarihi 2014",
    "tek corap, cift iddiasi reddedilmis",
]

MUHURLER = [
    "GORULDU",
    "UYGUNDUR AMA DEGILDIR",
    "IADE: EKSIK EK",
    "ASIL EVRAK ASILDIR",
    "BEKLETILDI, SEBEP: CEKMECE",
]


def ac(derinlik: int, rng: random.Random) -> str:
    if derinlik <= 0 or rng.random() < 0.18:
        return rng.choice(ICERIKLER)
    ic = ac(derinlik - 1, rng)
    return f"cekmece({ic})"


def ara(hedef: str, sabir: int, tohum: int | None) -> int:
    rng = random.Random(tohum)
    print("CEKMECE ICINDE CEKMECE")
    print("Mudurluk: Evici Cekmece Isleri Genel Mudurlugu")
    print(f"Aranan: {hedef}")
    print("-" * 42)
    for deneme in range(1, sabir + 1):
        derinlik = rng.randint(1, 5)
        bulunan = ac(derinlik, rng)
        muhur = rng.choice(MUHURLER)
        print(f"[{deneme}] {bulunan}")
        print(f"     muhur: {muhur}")
        if hedef.lower() in bulunan.lower() and rng.random() < 0.35:
            print("BULUNDU. Ama cekmece kapanirken yine kayboldu.")
            return 0
        if rng.random() < 0.12:
            print("DIKKAT: yeni bir cekmece dogdu. Nufus cuzdani yok.")
    print("-" * 42)
    print(f"Sonuc: {hedef} yok. Var olan sey sadece cekmece.")
    print("Cozum onerisi: bir cekmece daha ac. Ya da acma. Ikisi de resmi.")
    return 1


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(
        description="Tornavida arar, cekmece bulur. Bu bir ozelliktir."
    )
    p.add_argument("--hedef", default="tornavida", help="bulunmayacak nesne")
    p.add_argument("--sabir", type=int, default=6, help="kac cekmece acilacak")
    p.add_argument("--tohum", type=int, default=None, help="tekrarlanabilir kaos")
    args = p.parse_args(argv)
    if args.sabir < 1:
        print("Sabir sifirdan kucuk olamaz. Cekmece bile buna guler.")
        return 2
    return ara(args.hedef, args.sabir, args.tohum)


if __name__ == "__main__":
    sys.exit(main())
