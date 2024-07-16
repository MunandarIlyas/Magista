document
  .getElementById("quizForm")
  .addEventListener("submit", function (event) {
    event.preventDefault();

    // Mendapatkan nilai dari input nama dan grup
    var nama = document.getElementById("namaGrup").value;
    var grup = document.getElementById("kelasDropdown").value;

    // Mendapatkan nilai jawaban dari setiap pertanyaan
    var jawaban1 = document.querySelector(
      'input[name="question1"]:checked'
    ).value;
    var jawaban2 = document.querySelector(
      'input[name="question2"]:checked'
    ).value;
    var jawaban3 = document.querySelector(
      'input[name="question3"]:checked'
    ).value;
    var jawaban4 = document.querySelector(
      'input[name="question4"]:checked'
    ).value;
    var jawaban5 = document.querySelector(
      'input[name="question5"]:checked'
    ).value;

    var data = {
      Nama: nama,
      Grup: grup,
      "Jawaban Soal 1": jawaban1,
      "Jawaban Soal 2": jawaban2,
      "Jawaban Soal 3": jawaban3,
      "Jawaban Soal 4": jawaban4,
      "Jawaban Soal 5": jawaban5,
    };

    var jsonData = JSON.stringify(data);

    console.log(jsonData);

    // Membuat objek XMLHttpRequest
    var xhr = new XMLHttpRequest();

    // Mengatur metode, URL, dan header permintaan
    xhr.open("POST", "/quiz_submission/", true);
    xhr.setRequestHeader("Content-Type", "application/json");

    // Menangani respons dari server
    xhr.onreadystatechange = function () {
      if (xhr.readyState === XMLHttpRequest.DONE) {
        // Mengonversi respons dari server ke JSON
        var response = JSON.parse(xhr.responseText);
        console.log(response);

        // Membuat elemen dengan ID 'donekuis' muncul setelah formulir dikirim
        document.getElementById("donekuis").style.display = "block";
        document.getElementById("kuis").style.display = "none";
      }
    };

    // Mengirim data JSON ke server
    xhr.send(jsonData);

    // Di sini Anda dapat melakukan apa pun dengan nilai-nilai tersebut, seperti mengirimnya ke server, menyimpan di database, dll.
  });

// Menyimpan data dari formulir saat disubmit
document
  .getElementById("evalForm")
  .addEventListener("submit", function (event) {
    event.preventDefault(); // Menghentikan pengiriman formulir

    // Mengambil nilai dari setiap elemen input
    var nama = document.getElementById("eval_nama").value;
    var kelas = document.getElementById("kelasDropdown2").value;
    var jawaban1 = document.getElementById("jawaban1").value;
    var jawaban2 = document.getElementById("jawaban2").value;
    var jawaban3 = document.getElementById("jawaban3").value;
    var jawaban4 = document.getElementById("jawaban4").value;
    var jawaban5 = document.getElementById("jawaban5").value;
    var jawaban6 = document.getElementById("jawaban6").value;

    // Menyimpan data ke dalam objek untuk dikirimkan atau diproses lebih lanjut
    var data = {
      nama: nama,
      kelas: kelas,
      jawaban1: jawaban1,
      jawaban2: jawaban2,
      jawaban3: jawaban3,
      jawaban4: jawaban4,
      jawaban5: jawaban5,
      jawaban6: jawaban6,
    };

    var jsonData = JSON.stringify(data);

    console.log(jsonData);

    // Membuat objek XMLHttpRequest
    var xhr = new XMLHttpRequest();

    // Mengatur metode, URL, dan header permintaan
    xhr.open("POST", "/eval_submission/", true);
    xhr.setRequestHeader("Content-Type", "application/json");

    // Menangani respons dari server
    xhr.onreadystatechange = function () {
      if (xhr.readyState === XMLHttpRequest.DONE) {
        // Mengonversi respons dari server ke JSON
        var response = JSON.parse(xhr.responseText);
        console.log(response);

        // Membuat elemen dengan ID 'donekuis' muncul setelah formulir dikirim
        document.getElementById("doneEval").style.display = "block";
        document.getElementById("Eval").style.display = "none";

        // // Membuat elemen dengan ID 'donekuis' muncul setelah formulir dikirim
        // document.getElementById("donekuis").style.display = "block";
        // document.getElementById("kuis").style.display = "none";
      }
    };

    // Mengirim data JSON ke server
    xhr.send(jsonData);

    // Melakukan log data ke konsol
    console.log(
      "Formulir berhasil dikirim!\nNama: " + nama + "\nKelas: " + kelas
    );
  });
