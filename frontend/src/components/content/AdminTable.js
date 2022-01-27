import React, { Component } from 'react';
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import Paper from '@mui/material/Paper';
import Button from '@mui/material/Button';
import Input from '@mui/material/Input';

function createData(semester, edvnr, modul, sws, ects, prüfung) {
  return { semester, edvnr, modul, sws, ects, prüfung };
}

const rows = [

    createData(<strong>1</strong>, <strong>VS: 33500</strong>, <strong>Einstufungstest Englisch</strong>, <strong>0</strong>, <strong>0</strong>, <strong>VS: LÜ</strong>),
   
  
    createData(<b>1</b>, <b>PL: 335120</b>, <b>Marketing & Organisation</b>,<b>4</b>,<b>5</b>,<b>PL: KMP</b>),
    createData('','335120a','Marketing',2,2,'Language', 'Literature', 'Sources', 'Connection', 'Description',  'Workload', 'Professor' ),
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
  

]

export default class AdminTable extends Component {
  constructor(props){
    super(props)
    this.deleteRow = this.deleteRow.bind(this)
  }

  state = {
    editedCell: null,
    rows : rows,

    editedEdvNr: ''
  }

  deleteRow(index){
    // TOOD: send deleted row to backend with index or id
    this.setState({rows: this.state.rows.filter((row, i) => i !== index)})
  }

  saveChangedRow(){
    alert(this.state.editedEdvNr)
    // TODO: send data of changed row to backend
  }

  render(){
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
              <TableCell align="right">Bearbeiten</TableCell>
            </TableRow>
          </TableHead>
          <TableBody>
            {this.state.rows.map((row, index) => (
              <TableRow
                key={row.name}
                sx={{ '&:last-child td, &:last-child th': { border: 0 } }}
              >
                <TableCell component="th" scope="row">
                  {row.semester}
                </TableCell>
                <TableCell align="right">
                  {this.state.editedCell === index ?
                    <Input value={row.edvnr} onChange={e => this.setState({editedEdvNr: e.target.value})} />
                    : 
                    row.edvnr
                  }
                </TableCell>
                <TableCell align="right">
                  {this.state.editedCell === index ?
                    <Input value={row.modul} />
                    : 
                    row.modul
                  }
                </TableCell>
                <TableCell align="right">{row.sws}</TableCell>
                <TableCell align="right">{row.ects}</TableCell>
                <TableCell align="right">{row.prüfung}</TableCell>
                <TableCell align="right">
                  <Button onClick={() => this.setState({editedCell: index})}>Bearbeiten</Button>
                   <Button onClick={() => this.deleteRow(index)}>Löschen</Button>
                </TableCell>
              </TableRow>
            ))}
          </TableBody>
        </Table>
      </TableContainer>
    );
  }
} 

// Tabelle mit zum aufklappen
/* 
import * as React from 'react';
import PropTypes from 'prop-types';
import Box from '@mui/material/Box';
import Collapse from '@mui/material/Collapse';
import IconButton from '@mui/material/IconButton';
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import Typography from '@mui/material/Typography';
import Paper from '@mui/material/Paper';
import KeyboardArrowDownIcon from '@mui/icons-material/KeyboardArrowDown';
import KeyboardArrowUpIcon from '@mui/icons-material/KeyboardArrowUp';

function createData(name, edvnr, modul, sws, etcs, bearbeiten) {
  return {
    name,
    edvnr,
    modul,
    sws,
    etcs,
    bearbeiten,
    weiteres: [
      {
        etcspunkte: '2',
        swspunkte: '2',
        professorID: 'Wagner',
        buch: 'Wirtschaft',
        sprache: 'Deutsch',
        edvnummer: '234567a',
      },

      {
        etcspunkte: '3',
        swspunkte: '2',
        professorID: 'Müller',
        buch: 'Ökonomie',
        sprache: 'Deutsch',
        edvnummer: '234567b'
      },
    ],
  };
}



function Row(props) {
  const { row } = props;
  const [open, setOpen] = React.useState(false);



  return (
    <React.Fragment>
      <TableRow sx={{ '& > *': { borderBottom: 'unset' } }}>
        <TableCell>
          <IconButton
            aria-label="expand row"
            size="small"
            onClick={() => setOpen(!open)}
          >
            {open ? <KeyboardArrowUpIcon /> : <KeyboardArrowDownIcon />}
          </IconButton>
        </TableCell>
        <TableCell component="th" scope="row">
          {row.name}
        </TableCell>
        <TableCell align="right">{row.edvnr}</TableCell>
        <TableCell align="right">{row.modul}</TableCell>
        <TableCell align="right">{row.sws}</TableCell>
        <TableCell align="right">{row.etcs}</TableCell>
        <TableCell align="right">{row.bearbeiten}</TableCell>
        
      </TableRow>
      <TableRow>
        <TableCell style={{ paddingBottom: 0, paddingTop: 0 }} colSpan={6}>
          <Collapse in={open} timeout="auto" unmountOnExit>
            <Box sx={{ margin: 1 }}>
              <Typography variant="h6" gutterBottom component="div">
                Weiteres
              </Typography>
              <Table size="small" aria-label="purchases">
                <TableHead>
                  <TableRow>
                    <TableCell>ETCS-Punkte</TableCell>
                    <TableCell>SWS-Punkte</TableCell>
                    <TableCell>Professor</TableCell>
                    <TableCell>Buch</TableCell>
                    <TableCell>Sprache</TableCell>
                    <TableCell>EDV-Nr.</TableCell>
                  </TableRow>
                </TableHead>
                <TableBody>
                  {row.weiteres.map((weiteresRow) => (
                    <TableRow>
                      <TableCell align="right">{weiteresRow.etcspunkte}</TableCell>
                      <TableCell align="right">{weiteresRow.swspunkte}</TableCell>
                      <TableCell align="right">{weiteresRow.professorID}</TableCell>
                      <TableCell align="right">{weiteresRow.buch}</TableCell>
                      <TableCell align="right">{weiteresRow.sprache}</TableCell>
                      <TableCell align="right">{weiteresRow.edvnummer}</TableCell>  

                    </TableRow>
                  ))}
                </TableBody>
              </Table>
            </Box>
          </Collapse>
        </TableCell>
      </TableRow>
    </React.Fragment>
  );
}

Row.propTypes = {
  row: PropTypes.shape({
    edvnr: PropTypes.number.isRequired,
    sws: PropTypes.number.isRequired,
    modul: PropTypes.string.isRequired,
    weiteres: PropTypes.arrayOf(
      PropTypes.shape({
        buch: PropTypes.string.isRequired,
        professorID: PropTypes.string.isRequired,
        etcspunkte: PropTypes.string.isRequired,
        swspunkte: PropTypes.string.isRequired,
        sprache: PropTypes.string.isRequired,
      }),
    ).isRequired,
    name: PropTypes.string.isRequired,
    bearbeiten: PropTypes.number.isRequired,
    etcs: PropTypes.number.isRequired,
  }).isRequired,
};

const rows = [
  createData('1', 234567, 'Betriebswirtschaft', 4, 5, ''),
  createData('1', 448973, 'Design', 4, 5, ''),
];


export default function CollapsibleTable() {
  return (
    <TableContainer component={Paper}>
      <Table aria-label="collapsible table">
        <TableHead>
          <TableRow>
            <TableCell />
            <TableCell>Semester</TableCell>
            <TableCell align="right">EDV-Nr.</TableCell>
            <TableCell align="right">Modul (Kurzbezeichnung)</TableCell>
            <TableCell align="right">SWS</TableCell>
            <TableCell align="right">ECTS</TableCell>
            <TableCell align="right">Bearbeiten</TableCell>
          </TableRow>
        </TableHead>
        <TableBody>
          {rows.map((row) => (
            <Row key={row.name} row={row} />
          ))}
        </TableBody>
      </Table>
    </TableContainer>
  );
}*/