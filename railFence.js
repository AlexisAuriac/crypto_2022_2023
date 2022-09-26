function railFenceEncrypt(s, rows = 3) {
	const rails = [...new Array(rows)].map(_ => [])

	let currentRow = 0
	let down = true

	for (let i = 0; i < s.length; i++) {
		rails[currentRow].push(s[i])

		if (currentRow === 0) {
			down = true
		} else if (currentRow === rows - 1) {
			down = false
		}

		currentRow += down ? 1 : -1
	}

	console.log(s.length)
	console.log(rails.map(rail => rail.length))

	return rails.map(chars => chars.join('')).join('')
}

function railFenceDecrypt(s, rows = 3) {
	const sizeRails = [...new Array(rows)].map(_ => 0)
	const path = []

	let currentRow = 0
	let down = true

	for (let i = 0; i < s.length; i++) {
		path.push([currentRow, sizeRails[currentRow]])
		sizeRails[currentRow] += 1

		if (currentRow === 0) {
			down = true
		} else if (currentRow === rows - 1) {
			down = false
		}

		currentRow += down ? 1 : -1
	}

	const rails = sizeRails.map((size, i) => {
		const offset = sizeRails.slice(0, i).reduce((x, y) => x + y, 0)
		return s.slice(offset, offset + size)
	})

	return path.map(([row, col]) => rails[row][col]).join('')
}

function main() {
	if (process.argv.length <= 3) {
		console.log('USAGE:')
		console.log('\tnode railFence.js encrypted_string rows')
		process.exit(1)
	}

	const enc = process.argv[2]
	const rows = Number.parseInt(process.argv[3])

	console.log(railFenceDecrypt(enc, rows))
}

main()

// usage example:
// $ node railFence.js ctearrpogorpe.ry.ghf 3
// crypto.geographer.fr
