import { promises as fs } from 'fs'

import sha256 from 'js-sha256'

const allowed_chars = [...new Array('~'.charCodeAt(0) - ' '.charCodeAt(0) + 1)].map((_, i) => {
	return String.fromCodePoint(i + ' '.charCodeAt(0))
})

const logs = JSON.parse((await fs.readFile('logs.json')).toString()).data.requestsLog

const hashes = logs
	.filter(({name}) => name !== 'addConfession')
	.map(log => JSON.parse(log.args).hash)

function bruteForce(hash, flag) {
	for (let c of allowed_chars) {
		const testHash = sha256(flag + c)

		if (testHash === hash) {
			return flag + c
		}
	}

	return null
}

let flag = ''

for (let hash of hashes) {
	flag = bruteForce(hash, flag)

	if (flag === null) {
		console.log('Flag not found')
		break
	} else if (flag.match(/^BFS\{.+\}$/)) {
		console.log(flag)
		break
	}
}
