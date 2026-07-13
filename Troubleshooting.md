## Troubleshooting

**Exit143** 

Symptom: conda env create exits 143 after repodata.
Cause: process terminated externally (SIGTERM), not dependency solve failure.
Fix: run with mamba and detached logging; use conda-style pins in environment file.
Verify: env exists, activation succeeds, python path points to sampl env.