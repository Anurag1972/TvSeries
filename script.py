import cs50
import csv


open("shows4.db","w").close()
f=open("data.tsv","r")
reader=csv.DictReader(f,delimiter="\t")
db=cs50.SQL("sqlite:///shows4.db")
db.execute("CREATE TABLE tvshows(tconst TEXT ,primaryTitle TEXT,startYear NUMERIC,genres TEXT)")
for row in reader:
    if row["titleType"]=="tvSeries" and row["isAdult"]=="0":
        if row["startYear"] != "\\N":
            startyear=int(row["startYear"])
        if startyear >1990:
            tconst=row["tconst"]
            primarytitle=row["primaryTitle"]
            genres=row["genres"]
            db.execute("INSERT INTO tvshows(tconst,primaryTitle,startYear,genres) VALUES(?,?,?,?)",tconst ,primarytitle,startyear,genres)

