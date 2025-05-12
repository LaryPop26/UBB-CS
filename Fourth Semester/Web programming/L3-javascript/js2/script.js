document.getElementById("submitBtn").addEventListener("click", () => {
	const nameInput = document.getElementById("name");
	const birthdateInput = document.getElementById("birthdate");
	const ageInput = document.getElementById("age");
	const emailInput = document.getElementById("email");

	const name = nameInput.value.trim();
	const birthdate = birthdateInput.value.trim();
	const age = ageInput.value.trim();
	const email = emailInput.value.trim();

	const nameRegex = /^[A-Za-z\s.]+$/;
	const birthdateRegex = /^(0[1-9]|[12][0-9]|3[01])-(0[1-9]|1[012])-[1-2][0-9]{3}$/;
	const ageRegex = /^[1-9][0-9]{0,2}$/;
	const emailRegex = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-z]{2,}$/;

	[nameInput, birthdateInput, ageInput, emailInput].forEach(input => {
		input.classList.remove("invalid", "valid");
	});

	let campuriInvalide = [];

	if (!name || !nameRegex.test(name)) {
		campuriInvalide.push("nume");
		nameInput.classList.add("invalid");
	} else {
		nameInput.classList.add("valid");
	}

	let parsedBirthdate = null;
	if (!birthdate || !birthdateRegex.test(birthdate)) {
		campuriInvalide.push("data nasterii");
		birthdateInput.classList.add("invalid");
	} else {
		const parts = birthdate.split("-");
		const day = parseInt(parts[0], 10);
		const month = parseInt(parts[1], 10) - 1; 
		const year = parseInt(parts[2], 10);
		parsedBirthdate = new Date(year, month, day);
		birthdateInput.classList.add("valid");
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
		ageInput.classList.add("invalid");
	} else {
		ageInput.classList.add("valid");
	}

	if (!email || !emailRegex.test(email)) {
		campuriInvalide.push("email");
		emailInput.classList.add("invalid");
	} else {
		emailInput.classList.add("valid");
	}

	const message = document.getElementById("message");
	if (campuriInvalide.length === 0) {
		message.textContent = "Datele sunt completate corect.";
		message.style.color = "green";
	} else {
		message.textContent = "Campurile " + campuriInvalide.join(" și ") + " nu sunt completate corect.";
		message.style.color = "red";
	}
});
