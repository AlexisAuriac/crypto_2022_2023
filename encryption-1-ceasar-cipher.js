const testData = [
{
	data: ["CLOUD TABLE ENTER MACRO LOGIN", 2],
	result: "AJMSB RYZJC CLRCP KYAPM JMEGL"
},
{
	data: ["FRAME ARRAY PRINT INBOX POPUP", 21],
	result: "KWFRJ FWWFD UWNSY NSGTC UTUZU"
},
{
	data: ["LOGIC CLOUD MEDIA ARRAY CACHE", 21],
	result: "QTLNH HQTZI RJINF FWWFD HFHMJ"
},
{
	data: ["MODEM QUEUE ARRAY LOGIC EMAIL", 5],
	result: "HJYZH LPZPZ VMMVT GJBDX ZHVDG"
},
{
	data: ["MOUSE LOGIN SHELL POPUP QUEUE", 3],
	result: "JLRPB ILDFK PEBII MLMRM NRBRB"
}
]

// todo: handle keys >= 26 || keys < -26
function shift(c, key) {
	if (c.match(/([a-z]|[A-Z])/) === null) {
		return c
	}

	return String.fromCodePoint(c.codePointAt(0) - key)
}

function ceasarCipher([data, key]) {
	return data
		.split("")
		.map(c => shift(c, key))
		.join("")
}

function main() {
	for (let i = 1; i < 26; i++) {
		console.log(ceasarCipher(['Vmr suvrqixeksul urvbxqk xf', i]))

	}
}

main()
