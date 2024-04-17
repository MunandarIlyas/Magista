document.getElementById('quizForm').addEventListener('submit', function(event) {
    event.preventDefault();
    
    // Mendapatkan nilai dari input nama dan grup
    var nama = document.getElementById('namaGrup').value;
    var grup = document.getElementById('kelasDropdown').value;
    
    // Mendapatkan nilai jawaban dari setiap pertanyaan
    var jawaban1 = document.querySelector('input[name="question1"]:checked').value;
    var jawaban2 = document.querySelector('input[name="question2"]:checked').value;
    var jawaban3 = document.querySelector('input[name="question3"]:checked').value;
    var jawaban4 = document.querySelector('input[name="question4"]:checked').value;
    var jawaban5 = document.querySelector('input[name="question5"]:checked').value;

    var data = {
        "Nama": nama,
        "Grup": grup,
        "Jawaban Soal 1": jawaban1,
        "Jawaban Soal 2": jawaban2,
        "Jawaban Soal 3": jawaban3,
        "Jawaban Soal 4": jawaban4,
        "Jawaban Soal 5": jawaban5
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
            document.getElementById('donekuis').style.display = 'block';
            document.getElementById('kuis').style.display = 'none';
        }
    };
    
    // Mengirim data JSON ke server
    xhr.send(jsonData);
    
       
    // Di sini Anda dapat melakukan apa pun dengan nilai-nilai tersebut, seperti mengirimnya ke server, menyimpan di database, dll.
  });