#!/bin/env node

import { promises as fs } from 'fs'

import axios from 'axios'

const alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'.split('')

const subjectUrl = 'https://crypto.geographer.fr'
const key = 'XWVACFQMLDKGHJZBREISNTUOYP'.split('')
const subjectFile = './subject.md'

async function downloadFile() {
  return (await axios({
    method: 'get',
    url: subjectUrl,
  })).data
}

function decrypt(enc) {
	return enc
		.split('')
		.map(c => {
			const upper = c.toUpperCase()

			const idx = alphabet.findIndex(c2 => upper === c2)

			if (idx === -1) {
				return c
			}

			if (upper === c) {
				return key[idx]
			} else {
				return key[idx].toLowerCase()
			}
		})
		.join('')
}

async function main() {
	const enc = await downloadFile()
	const subject = decrypt(enc)

	await fs.writeFile(subjectFile, subject)
}

main()
