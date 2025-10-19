#!/usr/bin/env bun

/**
 * Generate reference documentation from OpenAPI schemas
 * This script uses tag-mappings.json to determine English filenames
 */

import { join } from "path";
import { mkdir } from "fs/promises";

// Path setup
const SCRIPT_DIR = import.meta.dir;
const PROJECT_ROOT = join(SCRIPT_DIR, "..");
const OPENAPI_DIR = join(PROJECT_ROOT, "openapi");
const OUTPUT_DIR = join(PROJECT_ROOT, "skill", "references");
const MAPPINGS_FILE = join(OPENAPI_DIR, "tag-mappings.json");

// Type definitions
interface Operation {
  method: string;
  operationId?: string;
  summary?: string;
  description?: string;
}

interface PathData {
  path: string;
  operations: Operation[];
}

interface TagMappings {
  [apiName: string]: {
    [tagName: string]: string;
  };
}

interface OpenAPISchema {
  tags?: Array<{ name: string; description?: string }>;
  paths: {
    [path: string]: {
      [method: string]: {
        tags?: string[];
        operationId?: string;
        summary?: string;
        description?: string;
      };
    };
  };
}

/**
 * Strip HTML tags from text
 */
function stripHtmlTags(text: string): string {
  return text.replace(/<[^>]*>/g, "");
}

/**
 * Extract endpoints by tag from OpenAPI schema
 */
function extractEndpointsByTag(
  schema: OpenAPISchema,
  tagName: string
): PathData[] {
  const results: PathData[] = [];

  for (const [path, pathItem] of Object.entries(schema.paths)) {
    const operations: Operation[] = [];

    for (const [method, operation] of Object.entries(pathItem)) {
      if (method === "parameters") continue;
      if (!operation.tags?.includes(tagName)) continue;

      operations.push({
        method: method.toUpperCase(),
        operationId: operation.operationId,
        summary: operation.summary,
        description: operation.description,
      });
    }

    if (operations.length > 0) {
      results.push({ path, operations });
    }
  }

  return results;
}

/**
 * Generate reference document for a single tag
 */
async function generateReference(
  apiName: string,
  schema: OpenAPISchema,
  tagName: string,
  englishName: string,
  prefix: string
): Promise<void> {
  const outputFile = join(OUTPUT_DIR, `${prefix}-${englishName}.md`);

  // Get tag description from schema
  const tag = schema.tags?.find((t) => t.name === tagName);
  const tagDesc = tag?.description ? stripHtmlTags(tag.description) : "";

  // Extract endpoints for this tag
  const endpoints = extractEndpointsByTag(schema, tagName);

  // Build endpoints markdown
  let endpointsMd = "";
  for (const { path, operations } of endpoints) {
    for (const { method, summary, description } of operations) {
      endpointsMd += `### ${method} ${path}\n\n`;
      endpointsMd += `**操作**: ${summary || ""}\n\n`;

      if (description) {
        let cleanDesc = stripHtmlTags(description)
          .replace(/\s+/g, " ")
          .trim();

        if (cleanDesc.length > 500) {
          cleanDesc = cleanDesc.substring(0, 500) + "...";
        }

        if (cleanDesc) {
          endpointsMd += `**説明**: ${cleanDesc}\n\n`;
        }
      }
    }
  }

  // Get schema basename
  const schemaBasename = `${apiName}-schema.json`;

  // Generate markdown document
  const markdown = `# ${tagName}

## 概要

${tagDesc}

## エンドポイント一覧

${endpointsMd}

## 参考情報

- freee API公式ドキュメント: https://developer.freee.co.jp/docs
- OpenAPIスキーマ: [${schemaBasename}](../../openapi/${schemaBasename})
`;

  await Bun.write(outputFile, markdown);
  console.log(`Generated: ${prefix}-${englishName}.md`);
}

/**
 * Process an API
 */
async function processApi(
  apiKey: string,
  schemaFile: string,
  prefix: string,
  mappings: TagMappings
): Promise<void> {
  console.log("");
  console.log(`Processing ${apiKey}...`);
  console.log("================================");

  // Read schema file
  const schemaText = await Bun.file(schemaFile).text();
  const schema: OpenAPISchema = JSON.parse(schemaText);

  // Get all tags from mappings
  const tagMappings = mappings[apiKey];
  if (!tagMappings) {
    console.log(`No mappings found for ${apiKey}`);
    return;
  }

  let count = 0;
  for (const [tagName, englishName] of Object.entries(tagMappings)) {
    if (englishName) {
      await generateReference(apiKey, schema, tagName, englishName, prefix);
      count++;
    }
  }

  console.log(`Generated ${count} files for ${apiKey}`);
}

/**
 * Main execution
 */
async function main() {
  try {
    console.log("Starting reference document generation...");
    console.log("========================================");

    // Check if mappings file exists
    const mappingsFile = Bun.file(MAPPINGS_FILE);
    if (!(await mappingsFile.exists())) {
      console.error(`Error: Tag mappings file not found: ${MAPPINGS_FILE}`);
      process.exit(1);
    }

    // Read mappings
    const mappingsText = await mappingsFile.text();
    const mappings: TagMappings = JSON.parse(mappingsText);

    // Create output directory
    await mkdir(OUTPUT_DIR, { recursive: true });

    // Process each API
    await processApi(
      "accounting-api",
      join(OPENAPI_DIR, "accounting-api-schema.json"),
      "accounting",
      mappings
    );
    await processApi(
      "hr-api",
      join(OPENAPI_DIR, "hr-api-schema.json"),
      "hr",
      mappings
    );
    await processApi(
      "invoice-api",
      join(OPENAPI_DIR, "invoice-api-schema.json"),
      "invoice",
      mappings
    );
    await processApi(
      "pm-api",
      join(OPENAPI_DIR, "pm-api-schema.json"),
      "pm",
      mappings
    );

    console.log("");
    console.log("========================================");
    console.log("Reference generation complete!");
    console.log(`Output directory: ${OUTPUT_DIR}`);
  } catch (error) {
    console.error("Error:", error);
    process.exit(1);
  }
}

// Run main function
main();
