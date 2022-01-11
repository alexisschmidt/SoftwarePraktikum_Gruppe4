import * as React from 'react';
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import Paper from '@mui/material/Paper';


function createData(semester, veranstaltungsart, sws, etcs, pl, fPV, nfPV ) {
  return { semester, veranstaltungsart, sws, etcs, pl, fPV, nfPV };
}

const rows = [
  createData('1', 'Pflichtveranstaltung', 24, 30, 5, 1, 1),
  createData('2', 'Pflichtveranstaltung', 26, 30, 5, 1, 0),
  createData('Summe Grundstudium', '',  50 , 60, '', '', ''), 
  createData('3', 'Pflichtveranstaltung', 27, 30, 5, 1, 0),
  createData('4', 'Pflichtveranstaltung', 25, 30, 5, 1, 0),
  createData('5', 'Praktisches Studiensemester', 0, 30, 0, 0, 1),
  createData('6', 'Pflichtveranstaltung', 0, 0, 0, 0, 0),
  createData('', 'Wahlveranstaltung', '', 30, '', '', ''),
  createData('7', 'Pflichtveranstaltung', 1, 3, 1, 0, 0),
  createData('', 'Wahlveranstaltung', '', 15, '', '', ''),
  createData('', 'Thesis', 0, 12, 1, 0, 0),
  createData('Summe Pflichtbereich des Hauptstudiums', '', 53, 105, '', '', ''),
  createData('Gesamt (Grundstudium + Hauptstudium)', '', '*', 210, '', '', ''),
  createData('* je nach individueller Belegung','', '', '','', '', '')
];

export default function SpoTableStudent2 () {
  return (
    <TableContainer component={Paper}>
      <Table sx={{ minWidth: 500 }} size="small" aria-label="a dense table">
          <TableHead>
          <TableRow>
            <TableCell>Semester</TableCell>
            <TableCell align="right">Veranstaltungsart</TableCell>
            <TableCell align="right">SWS</TableCell>
            <TableCell align="right">ETCS</TableCell>
            <TableCell align="right">PL</TableCell>
            <TableCell align="right">fPV</TableCell>
            <TableCell align="right">nfPV</TableCell>
          </TableRow>
        </TableHead>
        <TableBody>
          {rows.map((row) => (
            <TableRow
              key={row.semester}
              sx={{ '&:last-child , &:last-child ':{ border: 2} }}>
              <TableCell component="th" scope="row">
                {row.semester}
              </TableCell>
              <TableCell align="right">{row.veranstaltungsart}</TableCell>
              <TableCell align="right">{row.sws}</TableCell>
              <TableCell align="right">{row.etcs}</TableCell>
              <TableCell align="right">{row.pl}</TableCell>
              <TableCell align="right">{row.fPV}</TableCell>
              <TableCell align="right">{row.nfPV}</TableCell>
             
            </TableRow>
          ))}
        </TableBody>
      </Table>
    </TableContainer>
  );
}

