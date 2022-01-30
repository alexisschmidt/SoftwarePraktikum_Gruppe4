import * as React from "react";
import Radio from "@mui/material/Radio";
import RadioGroup from "@mui/material/RadioGroup";
import FormControlLabel from "@mui/material/FormControlLabel";
import FormControl from "@mui/material/FormControl";
import FormLabel from "@mui/material/FormLabel";
import Button from "@mui/material/Button";
import Stack from "@mui/material/Stack";

export default function AuswahlStudentAdmin() {
  const [value, setValue] = React.useState("student");

  const handleChange = (event) => {
    setValue(event.target.value);
  };

  return (
    <FormControl component="fieldset">
      <FormLabel component="legend">
        Sind Sie ein Student oder ein Dozent?
      </FormLabel>
      <RadioGroup
        aria-label="gender"
        name="controlled-radio-buttons-group"
        value={value}
        onChange={handleChange}
      >
        <FormControlLabel value="student" control={<Radio />} label="Student" />
        <FormControlLabel value="dozent" control={<Radio />} label="Dozent" />
        <Stack spacing={2} direction="row">
          <Button variant="contained">Weiter</Button>
        </Stack>
      </RadioGroup>
    </FormControl>
  );
}
