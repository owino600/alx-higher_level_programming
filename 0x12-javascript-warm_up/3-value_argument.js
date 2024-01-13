#!/usr/bin/node
if (ProcessingInstruction.argv[2] === undefined)
{
    console.log('No argument');
}
else{
    console.log(process.argv[2]);
}