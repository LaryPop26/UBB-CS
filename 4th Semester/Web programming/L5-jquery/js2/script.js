$(document).ready(function () {
    $("#submitBtn").on("click", function () {
        const nameInput = $("#name");
        const birthdateInput = $("#birthdate");
        const ageInput = $("#age");
        const emailInput = $("#email");

        const name = nameInput.val().trim();
        const birthdate = birthdateInput.val().trim();
        const age = ageInput.val().trim();
        const email = emailInput.val().trim();

        const nameRegex = /^[A-Za-z\s.]+$/;
        const birthdateRegex = /^(0[1-9]|[12][0-9]|3[01])-(0[1-9]|1[012])-[1-2][0-9]{3}$/;
        const ageRegex = /^[1-9][0-9]{0,2}$/;
        const emailRegex = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-z]{2,}$/;

        const inputs = [nameInput, birthdateInput, ageInput, emailInput];
        inputs.forEach(input => {
            input.removeClass("invalid valid");
        });

        let campuriInvalide = [];

        if (!name || !nameRegex.test(name)) {
            campuriInvalide.push("nume");
            nameInput.addClass("invalid");
        } else {
            nameInput.addClass("valid");
        }

        let parsedBirthdate = null;
        if (!birthdate || !birthdateRegex.test(birthdate)) {
            campuriInvalide.push("data nasterii");
            birthdateInput.addClass("invalid");
        } else {
            const parts = birthdate.split("-");
            const day = parseInt(parts[0], 10);
            const month = parseInt(parts[1], 10) - 1;
            const year = parseInt(parts[2], 10);
            parsedBirthdate = new Date(year, month, day);
            birthdateInput.addClass("valid");
        }

        let ageValid = false;
        if (!age || !ageRegex.test(age)) {
            ageValid = false;
        } else if (parsedBirthdate) {
            const today = new Date();
            let calculatedAge = today.getFullYear() - parsedBirthdate.getFullYear();
            const monthDiff = today.getMonth() - parsedBirthdate.getMonth();
            const dayDiff = today.getDate() - parsedBirthdate.getDate();

            if (monthDiff < 0 || (monthDiff === 0 && dayDiff < 0)) {
                calculatedAge--;
            }

            if (parseInt(age) === calculatedAge) {
                ageValid = true;
            }
        }

        if (!ageValid) {
            campuriInvalide.push("varsta");
            ageInput.addClass("invalid");
        } else {
            ageInput.addClass("valid");
        }

        if (!email || !emailRegex.test(email)) {
            campuriInvalide.push("email");
            emailInput.addClass("invalid");
        } else {
            emailInput.addClass("valid");
        }

        const message = $("#message");
        if (campuriInvalide.length === 0) {
            message.text("Datele sunt completate corect.").css("color", "green");
        } else {
            message.text("Campurile " + campuriInvalide.join(" și ") + " nu sunt completate corect.").css("color", "red");
        }
    });
});
