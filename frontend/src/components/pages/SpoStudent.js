import React from 'react'
import SpoText from '../content/SpoText'
import SpoTableStudent1 from '../content/SpoTableStudent1'
import SpoTableStudent2 from '../content/SpoTableStudent2'

const SpoStudent = () => {
    return (
        <div>
            <h1>Deine SPO Ansicht</h1>
            <SpoText />
            <SpoTableStudent1 />
            <SpoTableStudent2 />
        </div>
    )
}

export default SpoStudent
