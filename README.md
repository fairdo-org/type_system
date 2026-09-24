# FDO Type System

A flexible and extensible type system for FAIR Digital Objects (FDOs), enabling structured metadata management and validation.

## Structure

```
type-system/
├── type-system.json             # Main type system definition
├── examples/
│   ├── car_instance.json        # Minimal example instance
│   ├── vehicle_types.json       # Example: vehicle types with attributes
│   └── handle-implementation/   # Batch files for Handle System creation
├── tools/
│   ├── handle_validator.py        # Web-based validator UI
│   └── batch-generator.js    # Tool to generate handle batch files
└── README.md
```

## Usage

### Validate a Handle Instance

Call `tools/handle_validator.py <pid>`

### Generate Handle Batch Files from Type Defintions in Json

New attributes and profiles can be expressed in Json, see examples.
For handle implementation generate batch files using: 
  `python example/handle_implementation/create_handle_batch.py <input> <output> <action>`
You need to provide a `.env` file with the following parameters
```
NAME_OF_PRIVKEY=<the location of the privkey used for batch authentication>
ADMIN_KEY=<location of the pubkey for batch authentication  in the form >'300:111111111111:handle'
ADMIN_HANDLE = <admin handle used for HS_ADMIN>
ADMIN_INDEX = <index of pubkey fo HS_ADMIN>
PREFIX = <prefix to be used>
```

To create PIDs using the batchfile you need to download the Handle System and call:
  `handle-9.3.2/bin/hdl-genericbatch <batch-filename>`

To validate a PID call:
   `python  tools/handle_validator.py <pid>`

