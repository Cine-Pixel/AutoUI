import { useState, useEffect } from "react";
import { Grid, CircularProgress } from "@mui/material";

import InputForm from "./forms/InputForm";

import "./App.css";

function App() {
  // const [inputConfig, setInputConfig] = useState([]);
  // const [outputConfig, setOutputConfig] = useState([]);
  const [config, setConfig] = useState({});
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    setLoading(true);
    fetch("/api/config", {
      method: "GET",
      headers: { "Content-Type": "application/json" },
    })
      .then((response) => response.json())
      .then((data) => {
        // setInputConfig(data["input"]);
        // setOutputConfig(data["output"]);
        setConfig(data);
        setLoading(false);
      })
      .catch((err) => console.error(err));
  }, []);

  return (
    <>
      <h1>Index page</h1>
      <Grid container spacing={2}>
        {loading ? (
          <CircularProgress />
        ) : (
          <>
            <Grid item xs={12} md={6}>
              <InputForm inputConfig={config["input"]} />
            </Grid>

            <Grid item xs={12} md={6}>
              <InputForm inputConfig={config["input"]} />
            </Grid>
          </>
        )}
      </Grid>
    </>
  );
}

export default App;
