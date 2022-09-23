const testData = [
{
	data: ["INBOXENTERLINUXSHIFTARRAY", "HYPERLINK"],
	result: "PLQSOPVGOYJXRLIAUSMRPVILG"
},
{
	data: ["EMAILLOGICPASTEDEBUGPOPUP","DYNAMIC"],
	result: "HKNIXTQJGPPMAVHBRBGORRNHP"
},
{
	data: ["CLOUDMEDIAMACROLINUXMODEM", "COMPUTER"],
	result: "EZAJXFIUKOYPWKSCKBGMGHHVO"
},
{
	data: ["POPUPEMAILMEDIAENTERDEBUG", "DATABASE"],
	result: "SOIUQEEELLFEEISIQTXREETYJ"
},
{
	data: ["VIRUSLINUXPRINTEMAILFLASH", "COMMAND"],
	result: "XWDGSYLPIJBRVQVSYMIYINOET"
}
]

function shift(c, i, key) {
	const acp = "A".codePointAt(0)
	const zcp = "Z".codePointAt(0)
	const cp = c.codePointAt(0)

	const k = key.codePointAt(i % key.length) - acp

	if (cp + k > zcp) {
		return String.fromCodePoint(acp + (cp + k) - zcp - 1)
	}

	return String.fromCodePoint(cp + k)
}

function vigenereCipher([data, key]) {
	return data
		.split("")
		.map((c, i) => shift(c, i, key))
		.join("")
}

function main() {
	ns.tprint(vigenereCipher(testData[0].data))
}

main()
