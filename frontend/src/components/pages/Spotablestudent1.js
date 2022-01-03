import * as React from 'react';
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import Paper from '@mui/material/Paper';

function createData(semester, edvnr, modul, sws, ects, prüfung) {
  return { semester, edvnr, modul, sws, ects, prüfung };
}

const rows = [
  createData(<strong>1</strong>, <strong>VS: 33500</strong>, <strong>Einstufungstest Englisch</strong>, <strong>0</strong>, <strong>0</strong>, <strong>VS: LÜ</strong>),
 

  createData(<b>1</b>, <b>PL: 335120</b>, <b>Marketing & Organisation</b>,<b>4</b>,<b>5</b>,<b>PL: KMP</b>),
  createData('','335120a','Marketing',2,2,'' ),
  createData('','335120b','Organisation',2,3,''),
  createData('', '', '', '', '',''),

  createData(<b>1</b>,<b>PL:335121</b>,<b>Grundlagen Wirtschaftsinformatik</b>,<b>4</b> ,<b>5</b>,<b>PL: KMP</b>),
  createData('', '', '', '', '',''),

  createData(<b>1</b>,<b>PL:335122</b>,<b>Datenbanken Grundlagen</b>,<b>4</b>,<b>5</b>, <b>PL:KMP</b>),
  createData('','335122a','Vorlesung Datenbanken',2,2,''),
  createData('','335122b','Übung Datenbanken',2,3,''),
  createData('', '', '', '', '',''),

  createData(<b>1</b>,<b>PL:335123</b>,<b>Programmieren</b>,<b>4</b>,<b>5</b>,<b>PL:KMP</b>),
  createData('','335123a','Vorlesung Programmieren',2,2,''),
  createData('','335123b','Übung Programmieren',2,3,''),


  

];

export default function DenseTable() {
  return (
    <TableContainer component={Paper}>
      <Table sx={{ minWidth: 650 }} size="small" aria-label="a dense table">
        <TableHead>
          <TableRow>
            <TableCell>Semester</TableCell>
            <TableCell align="right">EDV-Nr.</TableCell>
            <TableCell align="right">Modul (Kurzbezeichnung)</TableCell>
            <TableCell align="right">SWS</TableCell>
            <TableCell align="right">ECTS</TableCell>
            <TableCell align="right">Prüfung</TableCell>
          </TableRow>
        </TableHead>
        <TableBody>
          {rows.map((row) => (
            <TableRow
              key={row.name}
              sx={{ '&:last-child td, &:last-child th': { border: 0 } }}
            >
              <TableCell component="th" scope="row">
                {row.semester}
              </TableCell>
              <TableCell align="right">{row.edvnr}</TableCell>
              <TableCell align="right">{row.modul}</TableCell>
              <TableCell align="right">{row.sws}</TableCell>
              <TableCell align="right">{row.ects}</TableCell>
              <TableCell align="right">{row.prüfung}</TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>
    </TableContainer>
  );
}