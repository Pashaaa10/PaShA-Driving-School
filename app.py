from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)
app.secret_key = "secret key"

# MySQL Configuration
db = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="root",
    database="scoala_de_soferi"
)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/add_cursant", methods=["GET", "POST"])
def add_cursant():
    if request.method == "POST":
        nume = request.form["nume"]
        prenume = request.form["prenume"]
        cnp = request.form["cnp"]
        telefon = request.form["telefon"]
        adresa = request.form["adresa"]
        email = request.form["email"]
        sex = request.form["sex"]
        cursor = db.cursor()
        query = "INSERT INTO cursanti (Nume, Prenume, CNP, Telefon, Adresa, email, sex) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        values = (nume, prenume, cnp, telefon, adresa, email, sex)
        cursor.execute(query, values)
        db.commit()
        return redirect("/")
    else:
        return render_template("add_cursant.html")
    
@app.route("/add_instructor", methods=["GET", "POST"])
def add_instructor():
    if request.method == "POST":
        nume = request.form["nume"]
        prenume = request.form["prenume"]
        cnp = request.form["cnp"]
        telefon = request.form["telefon"]
        email = request.form["email"]
        cursor = db.cursor()
        query = "INSERT INTO instructori (Nume, Prenume, CNP, Telefon, email) VALUES (%s, %s, %s, %s, %s)"
        values = (nume, prenume, cnp, telefon, email)
        cursor.execute(query, values)
        db.commit()
        return redirect("/")
    else:
        return render_template("add_instructor.html")

@app.route("/delete_cursant/<int:cursant_id>")
def delete_cursant(cursant_id):
    cursor = db.cursor()
    query = "DELETE FROM cursanti WHERE CursantID = %s"
    values = (cursant_id,)
    cursor.execute(query, values)
    db.commit()
    return redirect("/")

@app.route("/delete_instructor/<int:instructor_id>")
def delete_instructor(instructor_id):
    cursor = db.cursor()
    query = "DELETE FROM instructori WHERE InstructorID = %s"
    values = (instructor_id,)
    cursor.execute(query, values)
    db.commit()
    return redirect("/")

@app.route("/update_cursant/", methods=["GET", "POST"])
def update_cursant():
    if request.method == "POST":
        cursor = db.cursor()

        nume = request.form["nume"]
        prenume = request.form["prenume"]
        cnp = request.form["cnp"]
        telefon = request.form["telefon"]
        adresa = request.form["adresa"]
        email = request.form["email"]
        sex = request.form["sex"]

        query = "UPDATE cursanti SET Nume = %s, Prenume = %s, CNP = %s, Telefon = %s, Adresa = %s, email = %s, sex = %s WHERE CursantID = %s"
        values = (nume, prenume, cnp, telefon, adresa, email, sex, cursant_id)
        cursor.execute(query, values)
        db.commit()
        return redirect("/")
    else:
        return render_template("update_cursanti.html", cursant= cursant)

@app.route("/update_instructor/<int:instructor_id>", methods=["GET", "POST"])
def update_instructor(instructor_id):
    cursor = db.cursor()
    cursor.execute("SELECT * FROM instructori WHERE InstructorID = %s", (instructor_id,))
    instructor = cursor.fetchone()
    if request.method == "POST":
        nume = request.form["nume"]
        prenume = request.form["prenume"]
        cnp = request.form["cnp"]
        telefon = request.form["telefon"]
        email = request.form["email"]

        query = "UPDATE instructori SET Nume = %s, Prenume = %s, CNP = %s, Telefon = %s, email = %s WHERE InstructorID = %s"
        values = (nume, prenume, cnp, telefon, email, instructor_id)
        cursor.execute(query, values)
        db.commit()
        return redirect("/")
    else:
        return render_template("update_instructori.html", instructori=instructori)

@app.route("/afisare_cursanti")
def afisare_cursant():
    cursor = db.cursor()
    cursor.execute("SELECT CursantID, Nume, Prenume, CNP, Telefon, Adresa, email, sex FROM cursanti")
    cursanti = cursor.fetchall()
    return render_template("cursanti_list.html", cursanti=cursanti)

@app.route("/afisare_instructori")
def afisare_instructor():
    cursor = db.cursor()
    cursor.execute("SELECT InstructorID, Nume, Prenume, CNP, Telefon, email FROM instructori")
    instructori = cursor.fetchall()
    return render_template("instructori_list.html", instructori=instructori)

# Funcția pentru execuția interogărilor simple
def execute_statistici_simple():
    cursor = db.cursor()

    # Execută interogările simple
    cursor.execute("SELECT cursanti.Nume, cursanti.Prenume, categorii_permis.NumeCategorie, programari_examen.DataExamen FROM cursanti JOIN programari_examen ON cursanti.CursantID = programari_examen.CursantID JOIN categorii_permis ON programari_examen.CategorieID = categorii_permis.CategorieID;")
    result_1 = cursor.fetchall()

    cursor.execute("SELECT Cursanti.Nume, Cursanti.Prenume, rezultate_examen.NotaTeoretic, rezultate_examen.NotaPractic FROM Cursanti JOIN rezultate_examen ON Cursanti.CursantID = rezultate_examen.ProgramareID;")
    result_2 = cursor.fetchall()

    cursor.execute("SELECT Cursanti.Nume, Cursanti.Prenume, Cursanti.Telefon, Cursanti.email, programari_examen.DataExamen FROM Cursanti JOIN programari_examen ON Cursanti.CursantID = programari_examen.CursantID WHERE programari_examen.DataExamen = '2022-01-10';")
    result_3 = cursor.fetchall()

    cursor.execute("SELECT Cursanti.Nume, Cursanti.Prenume, categorii_permis.NumeCategorie FROM Cursanti JOIN programari_examen ON Cursanti.CursantID = programari_examen.CursantID JOIN categorii_permis ON programari_examen.CategorieID = categorii_permis.CategorieID JOIN rezultate_examen ON programari_examen.ProgramareID = rezultate_examen.ProgramareID WHERE rezultate_examen.NotaPractic >= 21;")
    result_4 = cursor.fetchall()

    cursor.execute("SELECT rezultate_examen.NumeAgent, rezultate_examen.AlteMentiuni, masini.Model FROM rezultate_examen JOIN programari_examen ON rezultate_examen.ProgramareID = programari_examen.ProgramareID JOIN masini ON programari_examen.MasinaID = masini.MasinaID WHERE rezultate_examen.NotaPractic < 21;")
    result_5 = cursor.fetchall()

    cursor.execute("SELECT Cursanti.Nume, Cursanti.Prenume, Cursanti.Telefon FROM Cursanti JOIN programari_examen ON Cursanti.CursantID = programari_examen.CursantID JOIN masini ON programari_examen.MasinaID = masini.MasinaID JOIN categorii_permis ON programari_examen.CategorieID = categorii_permis.CategorieID WHERE Cursanti.sex = 'F' AND categorii_permis.NumeCategorie = 'B';")
    result_6 = cursor.fetchall()

    # Închide cursorul
    cursor.close()

    return result_1, result_2, result_3, result_4, result_5, result_6

# Funcția pentru execuția interogărilor complexe
def execute_statistici_complexe():
    cursor = db.cursor()

    # Execută interogările complexe
    cursor.execute("SELECT instructori.Nume, instructori.Prenume, (SELECT COUNT(*) FROM programari_examen WHERE programari_examen.InstructorID = instructori.InstructorID) AS NumarCursanti FROM instructori;")
    result_7 = cursor.fetchall()

    cursor.execute("SELECT cursanti.Nume, cursanti.Prenume FROM cursanti WHERE CursantID IN (SELECT CursantID FROM rezultate_examen WHERE NotaTeoretic = (SELECT MAX(NotaTeoretic) FROM rezultate_examen));")
    result_8 = cursor.fetchall()

    cursor.execute("SELECT categorii_permis.NumeCategorie, COUNT(*) AS NumarCursanti FROM categorii_permis JOIN programari_examen ON categorii_permis.CategorieID = programari_examen.CategorieID GROUP BY categorii_permis.NumeCategorie;")
    result_9 = cursor.fetchall()

    cursor.execute("SELECT cursanti.Nume, cursanti.Prenume FROM cursanti JOIN programari_examen ON cursanti.CursantID = programari_examen.CursantID WHERE programari_examen.DataExamen IN (SELECT DataExamen FROM programari_examen WHERE InstructorID = 1);")
    result_10 = cursor.fetchall()

    # Închide cursorul
    cursor.close()

    return result_7, result_8, result_9, result_10

# Rute pentru afișarea statisticilor
@app.route("/statistici_simple")
def statistici_simple():
    statistici_result_simple = execute_statistici_simple()
    return render_template("statistici_simple.html", statistici_result_simple=statistici_result_simple)

@app.route("/statistici_complexe")
def statistici_complexe():
    statistici_result_complexe = execute_statistici_complexe()
    return render_template("statistici_complexe.html", statistici_result_complexe=statistici_result_complexe)

if __name__ == "__main__":
    app.run()