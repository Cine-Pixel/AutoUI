import { Grid } from "@mui/material";

import Button from "../components/Button";
import { TextBox, Number, Slider } from "../components/inputs";

const componentsMap = {
  TextBox,
  Number,
  Slider,
};

function InputForm({ inputConfig }) {
  // useEffect(() => {
  //   console.log(inputConfig);
  // }, []);

  const handleSubmit = (event) => {
    event.preventDefault();
    console.log(event.target.elements);
  };

  return (
    <form method="POST" className="form" onSubmit={handleSubmit}>
      <Grid container spacing={2}>
        {inputConfig.map((input, idx) => {
          const TargetComponent = componentsMap[input["component"]];
          const { component, ...props } = input;

          return (
            <Grid item xs={12} key={idx}>
              <TargetComponent {...props} />
            </Grid>
          );
        })}

        <Grid item xs={6}>
          <Button xs={6} variant="contained" color="secondary">
            Clear
          </Button>
        </Grid>
        <Grid item xs={6}>
          <Button type="submit" xs={6} variant="contained">
            Submit
          </Button>
        </Grid>
      </Grid>
    </form>
  );
}

export default InputForm;
