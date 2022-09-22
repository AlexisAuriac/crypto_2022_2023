import { promises as fs } from 'fs'

import sha256 from 'js-sha256'

const allowed_chars = [...new Array('~'.charCodeAt(0) - ' '.charCodeAt(0) + 1)].map((_, i) => {
	return String.fromCodePoint(i + ' '.charCodeAt(0))
})

let logs = JSON.parse((await fs.readFile('logs.json')).toString()).data.requestsLog

logs = logs.filter(({name}) => name !== 'addConfession').slice(0, 100)

logs = logs.map(log => {
	const args = JSON.parse(log.args)
	return {
		hash: args.hash
	}
})

const dictHashMsg = new Map()
const dictMsgHash = new Map()

function bruteForce(hash, known = '') {
	for (let c of allowed_chars) {
		const testHash = sha256(known + c)

		if (testHash === hash) {
			return known + c
		}
	}

	return null
}

let known = ''

logs.forEach(req => {
	const hash = req.hash

	const res = bruteForce(hash, known)

	if (res !== null) {
		req.msg = res
		known = res
	} else {
		req.msg = null
		console.log(known)
		process.exit(0)
	}
})
